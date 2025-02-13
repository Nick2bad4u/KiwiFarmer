# -*- coding: UTF-8 -*-

"""Classes for KikiFarms forum objects
"""

###############################################################################

from datetime import datetime

import requests
from bs4 import BeautifulSoup

###############################################################################

import logging
from kiwifarmer import functions

logger = logging.getLogger()

class Thread:
    """Class for initializing the scrape of a KiwiFarms thread.

    Parameters
    ----------
    thread_url : str
        URL of thread page
        e.g. ``'https://kiwifarms.st/threads/satanic-vampire-neo-nazis-atomwaffen-division-siegeculture.38120/'``
    """

    def __init__(self, thread_page):
        # store parsable BeautifulSoup object as class variable
        self.thread_page = thread_page

        # get thread url from soup
        self.thread_url = self.thread_page.find('link', {'rel': 'canonical'})['href']

        # store thread ID as class variable
        self.thread_id = functions.get_thread_id(thread_url=self.thread_url)

        # extract thread title and store as class variable
        self.thread_title = functions.get_thread_title(thread_page=self.thread_page)
        # extract thread last page and store as class variable
        self.thread_last_page = functions.get_thread_last_page(thread_page=self.thread_page)

        # extract section of HTML containing thread creation information
        self.creation = self.get_thread_creation(self.thread_page)

        # extract thread creator username and store as class variable
        self.thread_creator_username = functions.get_thread_creator_username(creation=self.creation)
        # extract thread creator user ID and store as class variable
        self.thread_creator_user_id = functions.get_thread_creator_user_id(creation=self.creation)
        # extract thread creation timestamp and store as class variable
        self.thread_timestamp = functions.get_thread_timestamp(creation=self.creation)

        # save all thread fields in a single dictionary, used for insertion into JSON file
        self.thread_insertion = {
            'thread_url': self.thread_url,
            'thread_id': self.thread_id,
            'thread_title': self.thread_title,
            'last_page': self.thread_last_page,
            'creator_username': self.thread_creator_username,
            'creator_user_id': self.thread_creator_user_id,
            'thread_timestamp': self.thread_timestamp
        }

    def get_thread_creation(self, thread_page):
        # Directly find the time tag with class 'u-dt'
        # logger.debug(f"Thread page content: {thread_page.prettify()}")
        return thread_page.find('time', {'class': 'u-dt'})

    def get_thread_content(self, thread_page):
        # Extract and return thread content
        content_div = thread_page.find('div', {'class': 'bbWrapper'})
        if content_div:
            return content_div.text
        else:
            logger.error("Div with class 'bbWrapper' not found.")
            return None
  #---------------------------------------------------------------------------#

###############################################################################


class Page:
    """Class for initializing the scrape of a single page in a KwiFarms thread.

    Parameters
    ----------
    page_url : str
      URL of a single page in a KiwiFarms thread
      e.g. ``'https://kiwifarms.st/threads/satanic-vampire-neo-nazis-atomwaffen-division-siegeculture.38120/page-2/'``
    """

    #---------------------------------------------------------------------------#

    def __init__(self, thread_page):
        # store parsable BeautifulSoup object as class variable
        self.thread_page = thread_page
        self.thread_id = self.extract_thread_id()
        self.thread_title = self.extract_thread_title()

    #---------------------------------------------------------------------------#

    def extract_thread_id(self):
        # Extract the thread_id from the thread_page
        thread_id_element = self.thread_page.find('meta', {'property': 'og:url'})
        if thread_id_element and 'content' in thread_id_element.attrs:
            thread_id_url = thread_id_element['content']
            # Extract the thread ID from the URL
            thread_id = thread_id_url.split('.')[-1].split('/')[0]
            return int(thread_id)
        return None

    def extract_thread_title(self):
        # Extract the thread_title from the thread_page
        thread_title_element = self.thread_page.find('meta', {'property': 'og:title'})
        if thread_title_element and 'content' in thread_title_element.attrs:
            return thread_title_element['content']
        return None

    def get_post_soups(self):
        """Generate a list of BeautifulSoup HTML snippets that each contain a
        KiwiFarms post.

        Returns
        -------
        list:
          List of BeautifulSoup HTML snippets that each contain a KiwiFarms post.
        """
        _post_soups = self.thread_page.find_all('div', {'class': "message-inner"})
        post_soups = [post_soup for post_soup in _post_soups if post_soup.find('article', {'class': 'message-body js-selectToQuote'})]
        return post_soups

    #---------------------------------------------------------------------------#

###############################################################################

class Post:
    """Class for initializing the scrape of a single post in a KwiFarms thread.

    Parameters
    ----------
    post_soup : bs4.element.Tag
      BeautifulSoup HTML snippet that contains a KiwiFarms post
    """

    #---------------------------------------------------------------------------#

    def __init__(self, post):
        # store BeautifulSoup HTML snippet as class variable
        self.post = post

        # Extract section of HTML containing post message information
        message = functions.get_post_message(post=self.post)

        # Extract blockquotes and blockquotes sources from message
        blockquotes_text, blockquotes_sources = functions.get_post_blockquotes(message=message)
        # Extract link URLs from message
        links, links_texts = functions.get_post_links(message=message)
        # Extract image URLs from message
        images = functions.get_post_images(message=message)

        # Extract message text from message
        self.post_text = functions.process_text(text=message)
        message.decompose()

        # Store thread ID as class variable
        self.thread_id = functions.get_post_thread_id(post=self.post)
        # Store post ID as class variable
        self.post_id = functions.get_post_id(post=self.post)
        # Store post author username as class variable
        self.post_author_username = functions.get_post_author_username(post=self.post)
        # Store post author user ID as class variable
        self.post_author_user_id = functions.get_post_author_user_id(post=self.post)
        # Store post timestamp as class variable
        self.post_timestamp = functions.get_post_timestamp(post=self.post)
        # Store post datetime as class variable
        self.post_datetime = functions.get_post_datetime(post=self.post)
        # Store post URL as class variable
        self.post_url = functions.get_post_url(post=self.post)

        # Save all post fields in a single dictionary, used for insertion into MySQL database
        self.post_insertion = {
            'thread_id': self.thread_id,
            'post_id': self.post_id,
            'post_url': self.post_url,
            'author_username': self.post_author_username,
            'author_user_id': self.post_author_user_id,
            'post_timestamp': self.post_timestamp,
            'post_text': self.post_text
        }

        # Save all post fields in a single dictionary, used as a document for an Elasticsearch instance
        self.post_es_document = {
            'thread_id': self.thread_id,
            'post_id': self.post_id,
            'post_url': self.post_url,
            'author_username': self.post_author_username,
            'author_user_id': self.post_author_user_id,
            'post_datetime': datetime.fromisoformat(self.post_datetime),
            'post_text': self.post_text,
            'links': links,
            'images': images
        }

        # Generate list of dicts for blockquote fields
        self.blockquote_insertions = self.generate_blockquote_insertions(blockquotes_text, blockquotes_sources)

        # Generate list of dicts for link fields
        self.link_insertions = self.generate_link_insertions(links, links_texts)

        # Generate list of dicts for image fields
        self.image_insertions = self.generate_image_insertions(images)

    #---------------------------------------------------------------------------#

    def generate_blockquote_insertions(self, blockquotes_text, blockquotes_sources):
        _blockquote_insertions = []
        for bqt, bqs in zip(blockquotes_text, blockquotes_sources):
            _d = {
                'thread_id': self.thread_id,
                'post_id': self.post_id,
                'author_user_id': self.post_author_user_id,
                'blockquote_text': functions.process_text(text=bqt),
                'blockquote_source': bqs
            }
            _blockquote_insertions.append(_d)
        return _blockquote_insertions

    def generate_link_insertions(self, links, links_texts):
        _link_insertions = []
        for link, link_text in zip(links, links_texts):
            if len(link) <= 2048:
                _d = {
                    'thread_id': self.thread_id,
                    'post_id': self.post_id,
                    'author_user_id': self.post_author_user_id,
                    'link_source': link,
                    'link_text': link_text
                }
                _link_insertions.append(_d)
        return _link_insertions

    def generate_image_insertions(self, images):
        _image_insertions = []
        for image in images:
            if len(image) <= 2048:
                _d = {
                    'thread_id': self.thread_id,
                    'post_id': self.post_id,
                    'author_user_id': self.post_author_user_id,
                    'image_source': image
                }
                _image_insertions.append(_d)
        return _image_insertions

    #---------------------------------------------------------------------------#

###############################################################################
class ReactionPage:

  """Class for initializing the scrape of all reactions to a KwiFarms post.

  Parameters
  ----------
  soup : bs4.element.Tag
    BeautifulSoup HTML document of entire reaction page

  """

  #---------------------------------------------------------------------------#

  def __init__( self,
    reaction_page ):

    # store parsable BeautifulSoup object as class variable
    self.reaction_page = reaction_page

    url = reaction_page.find( 'meta', {'property' : 'og:url' } )[ 'content' ]
    self.post_id = int( url.split( '/' )[ 4 ] )

  #---------------------------------------------------------------------------#

  def get_reaction_soups( self ):

    """Generate a list of BeautifulSoup HTML snippets that each contain a
    KiwiFarms reaction.

    Returns
    -------
    list:
      List of BeautifulSoup HTML snippets that each contain a KiwiFarms reaction.

    """

    return functions.get_reaction_list( reaction_page = self.reaction_page )

  #---------------------------------------------------------------------------#

###############################################################################

class Reaction:

  """Class for initializing the scrape of a single reaction to a KwiFarms post.

  Parameters
  ----------
  reaction_soup : bs4.element.Tag
    BeautifulSoup HTML snippet that contains a single KiwiFarms reaction
  post_id : int
    Unique post ID number of the post the reaction is to.

  """

  #---------------------------------------------------------------------------#

  def __init__( self,
    reaction,
    post_id ):

    # store BeautifulSoup HTML snippet as class variable
    self.reaction = reaction

    # store post ID as class variable, since it's not available in the
    # individual reaction and needs to be passed from the ReactionPage class
    self.post_id = post_id

    #.........................................................................#

    # store reaction author name as class variable
    self.reaction_author_username = functions.get_reaction_author_username( reaction = self.reaction )
    # store reaction author user ID as class variable
    self.reaction_author_user_id = functions.get_reaction_author_user_id( reaction = self.reaction )
    # store reaction ID as class variable
    self.reaction_id = functions.get_reaction_id( reaction = self.reaction )
    # store reaction name as class variable
    self.reaction_name = functions.get_reaction_name( reaction = self.reaction )
    # store reaction author timestamp as class variable
    self.reaction_timestamp = functions.get_reaction_timestamp( reaction = self.reaction )

    #.........................................................................#

    # save all reaction fields in a single dictionary, used for insertion into
    # MySQL database
    self.reaction_insertion = {
      'post_id' : self.post_id,
      'author_username' : self.reaction_author_username,
      'author_user_id' : self.reaction_author_user_id,
      'reaction_id' : self.reaction_id,
      'reaction_name' : self.reaction_name,
      'reaction_timestamp' : self.reaction_timestamp }

  #---------------------------------------------------------------------------#

###############################################################################

class User:

  """Class for initializing the scrape of a single KiwiFarms user.

  Parameters
  ----------
  user_page : bs4.element.Tag
    BeautifulSoup HTML snippet that contains a KiwiFarms user page

  """

  #---------------------------------------------------------------------------#

  def __init__( self,
    user_page ):

    # store BeautifulSoup HTML document as class variable
    self.user_page = user_page

    #.........................................................................#

    # store user username as class variable
    self.user_username = functions.get_user_username( user_page = self.user_page )
    # store user ID as class variable
    self.user_id = functions.get_user_id( user_page = self.user_page )
    # store user profile picture link as class variable
    self.user_image = functions.get_user_image( user_page = self.user_page )
    # store number of user messages as class variable
    self.user_messages = functions.get_user_messages( user_page = self.user_page )
    # store user reaction score as class variable
    self.user_reaction_score = functions.get_user_reaction_score( user_page = self.user_page )
    # store number of user points as class variable
    self.user_points = functions.get_user_points( user_page = self.user_page )
    # store "Joined" and "Last Seen" timestamps as class variables
    self.user_joined, self.user_last_seen = functions.get_user_timestamps( user_page = self.user_page )
    # store user blurb as class variable
    self.user_blurb = functions.get_user_blurb( user_page = self.user_page )
    # store user role as class variable
    self.user_role = functions.get_user_role( user_page = self.user_page )
    #.........................................................................#

    # save all user fields in a single dictionary, used for insertion into
    # MySQL database
    self.user_insertion = {
      'user_username' : self.user_username,
      'user_id' : self.user_id,
      'user_image' : self.user_image,
      'user_messages' : self.user_messages,
      'user_reaction_score' : self.user_reaction_score,
      'user_points' : self.user_points,
      'user_joined' : self.user_joined,
      'user_last_seen' : self.user_last_seen,
      'user_blurb' : self.user_blurb,
      'user_role' : self.user_role, }

    #.........................................................................#

  #---------------------------------------------------------------------------#

###############################################################################

class Following:

  """Class for initializing the scrape of the following of a single KiwiFarms user.

  Parameters
  ----------
  following_page : bs4.element.Tag
    BeautifulSoup HTML snippet that contains the "Following" page of a
    KiwiFarms user

  """

  #---------------------------------------------------------------------------#

  def __init__( self,
    following_page ):

    # store BeautifulSoup HTML document as class variable
    self.following_page = following_page

    #.........................................................................#

    # store user username as class variable
    self.user_id = functions.get_following_user_id( following_page = self.following_page )
    self.following_user_ids = functions.get_following_following_ids( following_page = self.following_page )

    # generate list of dicts for following fields
    #.........................................................................#

    # initialize list for storing following insertion dicts
    _following_insertions = list( )

    # loop over all following users
    for fid in self.following_user_ids:

      _d = {
        'user_id' : self.user_id,
        'following_user_id' : fid, }

      # append the following insertion dict to the list of dicts
      _following_insertions.append( _d )

    # save list of following insertions as class variable
    self.following_insertions = _following_insertions

    #.........................................................................#

  #---------------------------------------------------------------------------#

###############################################################################

class TrophyPage:

  """Class for initializing the scrape of all trophies of a single KiwiFarms user.

  Parameters
  ----------
  user_page : bs4.element.Tag
    BeautifulSoup HTML snippet that contains a KiwiFarms user page

  """

  #---------------------------------------------------------------------------#

  def __init__( self,
    user_page ):

    # store BeautifulSoup HTML document as class variable
    self.user_page = user_page

    # store user ID as class variable
    self.user_id = functions.get_user_id( user_page = self.user_page )

    self.get_trophy_soups( )

    _trophy_insertions = list( )

    for trophy in self.trophies:

      _d = {
        'user_id' : self.user_id,
        'trophy_name' : functions.get_trophy_name( trophy ),
        'trophy_description' : functions.get_trophy_description( trophy ),
        'trophy_points' : functions.get_trophy_points( trophy ),
        'trophy_time' : functions.get_trophy_time( trophy ), }

      _trophy_insertions.append( _d )

    self.trophy_insertions = _trophy_insertions

  #---------------------------------------------------------------------------#

  def get_trophy_soups( self ):

    """Generate a list of BeautifulSoup HTML snippets that each contain a
    trophy for a KiwiFarms post.

    Returns
    -------
    list:
      List of BeautifulSoup HTML snippets that each contain a trophy for a
      KiwiFarms user.

    """

    trophy_list = self.user_page.find( 'ol', { 'class' : 'listPlain' } )
    if trophy_list is None:
      self.trophies = list( )
    else:
      trophies = trophy_list.find_all( 'li', { 'class' : 'block-row' } )
      self.trophies = trophies

    #.........................................................................#

  #---------------------------------------------------------------------------#

###############################################################################