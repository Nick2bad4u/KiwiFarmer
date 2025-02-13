# -*- coding: UTF-8 -*-

"""Functions for extracting fields from BeautifulSoup and string objects
"""

###############################################################################

import re
import os
import sys

# Add the parent directory to the sys.path to import kiwifarmer module
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from bs4 import BeautifulSoup

from kiwifarmer import utils

# Thread field extraction functions
###############################################################################

def get_thread_id( thread_url ):

  """Extract thread ID from thread URL.

  Parameters
  ----------
  thread_url : str
    URL of thread page
    e.g. ``'https://kiwifarms.st/threads/satanic-vampire-neo-nazis-atomwaffen-division-siegeculture.38120/'``

  Returns
  -------
  int
    Thread ID of thread corresponding to thread URL
    e.g. ``38120``
  """

  s = thread_url.split( '.' )

  if len( s ) == 3:
    return int( s[ -1 ].split( '/' )[ 0 ] )
  else:
    return int( s[ -1 ].split( '/' )[ -2 ] )

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

def get_thread_title( thread_page ):

  """Extract thread title from thread BeautifulSoup object.

  Parameters
  ----------
  thread_page : bs4.BeautifulSoup
    BeautifulSoup object containing parsable representation of HTML for first
    page of thread

  Returns
  -------
  str
    Thread title
    e.g. ``'Satanic Vampire Neo-Nazis (Atomwaffen Division & Siegeculture) - AKA autistic Strasserists AKA Helter Skelter cult'``
  """

  return str( thread_page.find('title').text )

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

def get_thread_last_page( thread_page ):

  """Extract number of thread pages from thread BeautifulSoup object.

  Parameters
  ----------
  thread_page : bs4.BeautifulSoup
    BeautifulSoup object containing parsable representation of HTML for first
    page of thread

  Returns
  -------
  int
    Number of pages in the thread
    e.g. ``64``

  """

  found = thread_page.find('div', {'class' : "inputGroup inputGroup--numbers inputNumber"} )

  if found is None:
    # thread is only a single page
    return 1
  else:
    return int( found.input['max'] )

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

def get_thread_creation( thread_page ):

  """Extract snippet of HTML that contains creation information
  from thread BeautifulSoup object.

  Parameters
  ----------
  thread_page : bs4.BeautifulSoup
    BeautifulSoup object containing parsable representation of HTML for first
    page of thread

  Returns
  -------
  bs4.element.Tag
    BeautifulSoup of HTML snippet that containins creation information

  """

  return thread_page.find('ul', {'class' : 'listInline listInline--bullet'})

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

def get_thread_creator_username( creation ):

  """Extract thread creator username from BeautifulSoup of HTML snippet
  containing creation information.

  Parameters
  ----------
  creation : bs4.element.Tag
    BeautifulSoup of HTML snippet that containins creation information

  Returns
  -------
  str
    Username of thread creator
    e.g. ``'Jewed Hunter'``

  """

  tmp = creation.find('a', {'class' : 'username u-concealed'})

  if tmp is None:
    return None

  else:
    return str( tmp.text )

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

def get_thread_creator_user_id( creation ):

  """Extract thread creator user ID from BeautifulSoup of HTML snippet
  containing creation information.

  Parameters
  ----------
  creation : bs4.element.Tag
    BeautifulSoup of HTML snippet that containins creation information

  Returns
  -------
  int
    User ID of thread creator
    e.g. ``20165``

  """

  tmp = creation.find('a', {'class' : 'username u-concealed'})

  if tmp is None:
    return None
  else:
    return int( tmp['data-user-id'] )

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

import logging

logger = logging.getLogger()

def get_thread_timestamp(creation):
    try:
        logger.debug(f"Creation content: {creation}")
        if creation:
            return int(creation['data-time'])
        else:
            logger.error("Time tag with class 'u-dt' not found.")
    except Exception as e:
        logger.error(f"Exception occurred while getting thread timestamp: {e}")
    return None

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

def get_thread_subforum( thread_page ):

  """Extract subforum path from BeautifulSoup of HTML snippet
  containing thread information.

  Parameters
  ----------
  thread_page : bs4.BeautifulSoup
    BeautifulSoup object containing parsable representation of HTML for first
    page of thread

  Returns
  -------
  str
    Timestamp of thread creation
    e.g. ``'Forums/Lolcow Salon/Amberlynn Reid'``

  """

  breadcrumbs = thread_page.find( 'div', { 'class' : 'block block--breadcrumbs' } )
  subforum = '/'.join( [ s.text for s in breadcrumbs.find_all( 'span' ) ] )

  return subforum

# Page field extraction functions
###############################################################################

def get_page_thread_id( page_url ):

  """Extract thread ID from page URL.

  Parameters
  ----------
  page_url : str
    URL of thread page
    e.g. ``'https://kiwifarms.st/threads/satanic-vampire-neo-nazis-atomwaffen-division-siegeculture.38120/page-2/'``

  Returns
  -------
  int
    Thread ID of thread corresponding to thread for page URL
    e.g. ``38120``
  """

  return int( page_url.split('/')[-3].split('.')[-1] )

# Post field extraction functions
###############################################################################

def get_post_thread_id( post ):

  """Extract thread ID from post BeautifulSoup object.

  Parameters
  ----------
  post : bs4.element.Tag
    BeautifulSoup object containing parsable representation of HTML for a post
    in the thread

  Returns
  -------
  int
    Thread ID of thread that `post` came from
    e.g. ``38120``

  """

  return post.find('a', {'rel':"nofollow"})[ 'href' ].split('/')[-2].split('.')[-1]

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

def get_post_id( post ):

  """Extract post ID from post BeautifulSoup object.

  Parameters
  ----------
  post : bs4.element.Tag
    BeautifulSoup object containing parsable representation of HTML for a post
    in the thread

  Returns
  -------
  int
    Post ID of post
    e.g. ``2924919``

  """

  return int( post.find('div', {'class' : 'message-userContent lbContainer js-lbContainer'}).attrs['data-lb-id'][5:] )

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

def get_post_author_username( post ):

  """Extract post author username from post BeautifulSoup object.

  Parameters
  ----------
  post : bs4.element.Tag
    BeautifulSoup object containing parsable representation of HTML for a post
    in the thread

  Returns
  -------
  str or None
    Username of post author
    e.g. ``'Jewed Hunter'``
    If post was made by a guest user, returns ``None``

  """

  try:
    return post.find('a', {'class' : 'username'}).text
  except AttributeError:
    return None

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

def get_post_author_user_id( post ):

  """Extract post author username from post BeautifulSoup object.

  Parameters
  ----------
  post : bs4.element.Tag
    BeautifulSoup object containing parsable representation of HTML for a post
    in the thread

  Returns
  -------
  str or None
    Username of post author
    e.g. ``'Jewed Hunter'``
    If post was made by a guest user, returns ``None``

  """

  try:
    return int( post.find('a', {'class' : 'username'})['data-user-id'] )
  except TypeError:
    return None

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

def get_post_timestamp( post ):

  """Extract post creation timestamp from post BeautifulSoup object.

  Parameters
  ----------
  post : bs4.element.Tag
    BeautifulSoup object containing parsable representation of HTML for a post
    in the thread

  Returns
  -------
  int
    Timestamp of post creation
    e.g. ``1515211698``

  """

  return int( post.find('time', {'class' : "u-dt" } )['data-time'] )

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

def get_post_datetime( post ):

  """Extract post creation datetime from post BeautifulSoup object.

  Parameters
  ----------
  post : bs4.element.Tag
    BeautifulSoup object containing parsable representation of HTML for a post
    in the thread

  Returns
  -------
  int
    Datetime of post creation
    e.g. ``'2021-03-04T22:55:38-0600'``

  """

  s = post.find('time', {'class' : "u-dt" } )['datetime']

  # Convert to proper ISO 8601 format
  return s[ :-2 ] + ':' + s[ -2 : ]

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

def get_post_url( post ):

  """Extract post url from post BeautifulSoup object.

  Parameters
  ----------
  post : bs4.element.Tag
    BeautifulSoup object containing parsable representation of HTML for a post
    in the thread

  Returns
  -------
  url
    URL of post
    e.g. ``'https://kiwifarms.st/threads/john-cameron-denton-atomwaffen-division-siegeculture.38120/post-2924919'``

  """

  url = post.find( 'a', { 'rel' : 'nofollow' } )[ 'href' ]

  url = 'https://kiwifarms.st' + url

  return url

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

def get_post_message( post ):

  """Extract snippet of HTML that contains message information
  from post BeautifulSoup object.

  Parameters
  ----------
  post : bs4.element.Tag
    BeautifulSoup object containing parsable representation of HTML for a post
    in the thread

  Returns
  -------
  bs4.element.Tag
    BeautifulSoup of HTML snippet that containins post message information

  """

  message = post.find('article', {'class' : 'message-body js-selectToQuote'})

  scripts = message.find_all( 'script' )
  for script in scripts:
    script.decompose()

  return message

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

def get_post_links( message ):

  """Extract list of hyperlinks from message BeautifulSoup object, and remove the hyperlink tags from the message object.

  Parameters
  ----------
  message : bs4.element.Tag
    BeautifulSoup object containing parsable representation of HTML for the
    message of the post.

  Returns
  -------
  list
    List of hyperlinks contained in the forum post

  """

  # find all hyperlink tags in `message`
  links = message.find_all( 'a', {'class' : 'link'})

  # create a list of links from all hyperlinks
  links_hrefs = [ str( link['href'] ) for link in links ]

  # create a list of link text from all hyperlinks
  links_texts = [ str( link.text ) for link in links ]

  # loop over all hyperlinks and remove them from the `message` object
  for l in links:
    l.decompose()

  return links_hrefs, links_texts

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

def get_post_blockquotes( message ):

  """Extract list of blockquotes and their sources from message BeautifulSoup
  object, and remove the blockquote tags from the message object.

  Parameters
  ----------
  message : bs4.element.Tag
    BeautifulSoup object containing parsable representation of HTML for the
    message of the post.

  Returns
  -------
  tuple
    Tuple containing two elements: list of blockquotes contained in the forum post, and the corresponding sources of the blockquotes.
    An example source is ``'#post-2927009'``, indicating that the post in question quoted the post with port ID ``'2927009'``.

  """

  # find all blockquote tags in `message`
  blockquotes = message.find_all('blockquote', {'class' : "bbCodeBlock bbCodeBlock--expandable bbCodeBlock--quote js-expandWatch"})

  # extract text for all blockquotes
  blockquotes_text = [ str( blockquote.find('div', {'class' : "bbCodeBlock-expandContent js-expandContent"}).text ) for blockquote in blockquotes ]

  # initialize list of blockquote sources
  blockquotes_sources = [ ]

  # loop over all blockquotes, populate list with blockquote source if it exists
  for blockquote in blockquotes:
    try:
      source = str( blockquote.find('a', {'class':"bbCodeBlock-sourceJump"}).get('data-content-selector') )
    except:
      source = None
    blockquotes_sources.append(source)

  # loop over all blockquotes and remove them from the `message` object
  for blockquote in blockquotes:
    blockquote.decompose()

  return blockquotes_text, blockquotes_sources

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

def get_post_images( message ):

  """Extract list of image URLs from message BeautifulSoup object, and remove the image container tags from the message object.

  Parameters
  ----------
  message : bs4.element.Tag
    BeautifulSoup object containing parsable representation of HTML for the
    message of the post.

  Returns
  -------
  list
    List of image URLs contained in the forum post

  """

  # find all image tags in `message`
  images = message.find_all('div', {'class' : "bbImageWrapper js-lbImage"})
  image_urls = [ str( image.find('img', {'class' : [ 'bbImage', 'bb' ]})['src'] ) for image in images]

  # loop over all images and remove them from the `message` object
  for image in images:
    image.decompose()

  return image_urls

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

def process_text( text ):

  """Sanitize text by removing unnecessary whitespace.

  Parameters
  ----------
  text : str or bs4.element.Tag
    String or BeautifulSoup object containing text information

  Returns
  -------
  str
    Sanitized version of input text
  """

  # if input `text` argument is not a string, assume it's a `bs4.element.Tag`
  # object, and extract the text postion of it
  if not isinstance( text, str):
    text = text.text

  # replace newlines and non-breaking spaces with periods. This is done in
  # order to preserve the implicit sentence structure of posts, e.g. when
  # newlines are used instead of periods to delimit sentences.
  text = text.replace('\n', '.').replace('\xa0', '.')

  # use regex to convert any sequence of 2 or more periods to a single
  # period followed by a space
  text = re.sub(r'\.{2,100}', '. ', text)

  # strip extraneous characters from the start and end of the string
  text = str( text.lstrip('. ').rstrip( ' ' ) )

  return text

# Reaction field extraction functions
###############################################################################

def get_reaction_list( reaction_page ):

  """Extract list of reactions from the raw HTML of the reaction page
  BeautifulSoup object.

  Parameters
  ----------
  reaction_page : bs4.element.Tag
    BeautifulSoup object containing parsable representation of HTML for first
    page of reaction

  Returns
  -------
  list
    List of reactions to the given post

  """

  all_reactions = reaction_page.find(
    'ol', { 'class' : 'block-body js-reactionList-0' } )

  if all_reactions is None:
    reaction_list = list( )
  else:
    reaction_list = all_reactions.find_all(
      'li', { 'class' : 'block-row block-row--separated' } )

  return reaction_list

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

def get_reaction_author_username( reaction ):

  """Extract the reactor username for a single reaction

  Parameters
  ----------
  reaction : bs4.element.Tag
    BeautifulSoup object containing parsable representation of HTML for a
    reaction to a post.

  Returns
  -------
  str
    Username of thread creator
    e.g. ``'Jewed Hunter'``
  """

  url = reaction.find(
      'a',
      {'class' : [
        'avatar avatar--s',
        'avatar avatar--s avatar--default avatar--default--dynamic' ] } )[ 'href' ]

  return url.split( '/' )[ 2 ].split( '.' )[ 0 ]

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

def get_reaction_author_user_id( reaction ):

  """Extract the reactor user ID for a single reaction

  Parameters
  ----------
  reaction : bs4.element.Tag
    BeautifulSoup object containing parsable representation of HTML for a
    reaction to a post.

  Returns
  -------
  int
    User ID of thread creator
    e.g. ``20165``
  """

  return int( reaction.find(
    'a',
    {'class' : [
      'avatar avatar--s',
      'avatar avatar--s avatar--default avatar--default--dynamic' ] } )['data-user-id'] )

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

def get_reaction_id( reaction ):

  """Extract the reaction ID for a single reaction

  Parameters
  ----------
  reaction : bs4.element.Tag
    BeautifulSoup object containing parsable representation of HTML for a
    reaction to a post.

  Returns
  -------
  int
    ID of reaction
    e.g. ``7`` (corresponds to ``'Feels'`` reaction)
  """

  return int( reaction.find(
    'div',
    { 'class' : 'contentRow-extra' } ).find( 'span' )[ 'data-reaction-id' ] )

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

def get_reaction_name( reaction ):

  """Extract the reaction ID for a single reaction

  Parameters
  ----------
  reaction : bs4.element.Tag
    BeautifulSoup object containing parsable representation of HTML for a
    reaction to a post.

  Returns
  -------
  int
    ID of reaction
    e.g. ``'Feels'`` (corresponds to reaction ID ``7``)
  """

  return reaction.find(
    'div',
    { 'class' : 'contentRow-extra' } ).find( 'span' ).find( 'img' )[ 'alt' ]

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

def get_reaction_timestamp( reaction ):

  """Extract reaction timestamp from BeautifulSoup of HTML snippet
  containing reaction information.

  Parameters
  ----------
  reaction : bs4.element.Tag
    BeautifulSoup of HTML snippet that containins reaction information

  Returns
  -------
  int
    Timestamp of reaction
    e.g. ``1515211698``

  """

  return int( reaction.find( 'time' )[ 'data-time' ] )

# User field extraction functions
###############################################################################

def get_user_username( user_page ):

  """Extract username from BeautifulSoup of HTML snippet
  containing user information.

  Parameters
  ----------
  user_page : bs4.element.Tag
    BeautifulSoup of HTML snippet that containins user information

  Returns
  -------
  str
    User's username
    e.g. ``'null'``

  """

  url = user_page.find( 'meta', {'property' : 'og:url' } )[ 'content' ]
  return url.split( '/')[ -2 ].split( '.' )[ 0 ]

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

def get_user_id( user_page ):

  """Extract user ID from BeautifulSoup of HTML snippet
  containing user information.

  Parameters
  ----------
  user_page : bs4.element.Tag
    BeautifulSoup of HTML snippet that containins user information

  Returns
  -------
  int
    User's user ID
    e.g. ``1``

  """

  url = user_page.find( 'meta', {'property' : 'og:url' } )[ 'content' ]
  return int( url.split( '/')[ -2 ].split( '.' )[ -1 ] )

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

def get_user_image( user_page ):

  """Extract profile picture image link from BeautifulSoup of HTML snippet
  containing user information.

  Parameters
  ----------
  user_page : bs4.element.Tag
    BeautifulSoup of HTML snippet that containins user information

  Returns
  -------
  str
    Link of user's profile image
    e.g. ``'https://no-cookie.kiwifarms.st/data/avatars/o/0/1.jpg?1578406498'``

  """

  avatar = user_page.find('a', {'class' : 'avatar avatar--l' } )

  if avatar is None:
    image = None
  else:
    image = avatar[ 'href']
  return image

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

def get_user_messages(user_page):
    messages_element = user_page.find('dl', class_='pairs pairs--rows pairs--rows--centered fauxBlockLink')
    if messages_element:
        message_count = messages_element.find('dd').find('a')
        if message_count:
            message_text = message_count.text.strip().replace('\n', '').replace('\t', '').replace(',', '')
            return utils.string_to_int(message_text)
    return 0

def get_user_reaction_score(user_page):
    reaction_score_element = user_page.find('dl', class_='pairs pairs--rows pairs--rows--centered')
    if reaction_score_element:
        score = reaction_score_element.find('dd')
        if score:
            score_text = score.text.strip().replace('\n', '').replace('\t', '').replace(',', '')
            return score_text  # Return the text directly as it's not a numeric value
    return "Unknown"

def get_user_points(user_page):
    # Find all <dl> elements with the class 'pairs pairs--inline'
    points_elements = user_page.find_all('dl', {'class': 'pairs pairs--inline'})

    # Iterate through the elements to find the one with "Points"
    for element in points_elements:
        dt = element.find('dt')
        if dt and dt.text.strip() == "Points":
            dd = element.find('dd')
            if dd:
                # Extract the points value and clean it
                points_text = dd.text.strip().replace('\n', '').replace('\t', '').replace(',', '')
                return utils.string_to_int(points_text)

    # If no points element is found, return 0
    return 0
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

def get_user_timestamps( user_page ):

  """Extract "Joined" and "Last Seen" timestamps from BeautifulSoup of HTML snippet
  containing user information.

  Parameters
  ----------
  user_page : bs4.element.Tag
    BeautifulSoup of HTML snippet that containins user information

  Returns
  -------
  tuple of int
    "Joined" and "Last Seen" timestamps of user
    e.g. ``1352899026, 1583634317``

  """

  dls = user_page.find_all( 'dl', {'class' : 'pairs pairs--inline' } )
  _udt = [ e.find( 'time', {'class' : 'u-dt'}) for e in dls ]
  udt = list( filter( None, _udt ))

  timestamps = [ int( dt[ 'data-time' ] ) for dt in udt ]

  if len( timestamps ) == 1:
    timestamps.append( None )

  return timestamps

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

def get_user_blurb( user_page ):

  """Extract user blurb from BeautifulSoup of HTML page
  containing user information.

  Parameters
  ----------
  user_page : bs4.element.Tag
    BeautifulSoup of HTML snippet that containins user information

  Returns
  -------
  str
    String of user blurb.
    e.g. ``'Ooperator'``

  """

  f = user_page.find( 'span', { 'class' : 'userTitle' } )

  if f is None:
    return None
  else:
    return f.text

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

def get_user_role( user_page ):

  """Extract user role/title from BeautifulSoup of HTML page
  containing user information.

  Parameters
  ----------
  user_page : bs4.element.Tag
    BeautifulSoup of HTML snippet that containins user information

  Returns
  -------
  str
    String of user role. If user has multiple roles, the roles are
    comma-delimited.
    e.g. ``'Founder,Retired Staff'``

  """

  ems = user_page.find_all( 'em', { 'class' : 'userBanner userBanner userBanner--primary' } )

  if ems == list( ):
    return None
  else:
    return ','.join( [ em.text for em in ems ] )

# Following field extraction functions
###############################################################################

def get_following_user_id(following_page):
    """Get the ID of the user, from BeautifulSoup of HTML document containing
    user following information

    Parameters
    ----------
    following_page : bs4.element.Tag
        BeautifulSoup of HTML snippet that contains user following information

    Returns
    -------
    int
        Member ID of user
        e.g. ``32976``
    """
    meta_tag = following_page.find('meta', {'property': 'og:url'})
    if not meta_tag:
        raise ValueError("Meta tag with property 'og:url' not found")

    url = meta_tag.get('content', '')
    if not url:
        raise ValueError("Content attribute in meta tag is empty")

    try:
        user_id = int(url.split('/')[-3])
    except (IndexError, ValueError) as e:
        raise ValueError(f"Failed to extract user ID from URL: {url}") from e

    return user_id

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

def get_following_following_ids(following_page):
    """Get the IDs of all users that the user follows, from BeautifulSoup of HTML
    document containing user following information

    Parameters
    ----------
    following_page : bs4.element.Tag
        BeautifulSoup of HTML snippet that contains user following information

    Returns
    -------
    list of int
        List of member IDs for all users that the user follows
        e.g. ``32976``
    """
    body = following_page.find('ol', {'class': 'block-body'})
    if not body:
        raise ValueError("Body with class 'block-body' not found")

    users = body.find_all('li', {'class': 'block-row block-row--separated'})
    user_ids = []
    for user in users:
        user_link = user.find('a', {'class': 'avatar avatar--s'})
        if user_link and 'data-user-id' in user_link.attrs:
            user_id = user_link['data-user-id']
            if user_id.isdigit():
                user_ids.append(int(user_id))
            else:
                raise ValueError(f"Non-numeric user ID found: {user_id}")
        else:
            raise ValueError("User link not found or does not contain 'data-user-id'")

    return user_ids
# Trophy field extraction functions
###############################################################################

def get_trophy_points( trophy ):

  """Get the number of points corresponding to a user's trophy, from
  BeautifulSoup of HTML snippet containing information for one trophy

  Parameters
  ----------
  trophy : bs4.element.Tag
    BeautifulSoup of HTML snippet that contains information for one trophy

  Returns
  -------
  int
    Number of points corres
    e.g. ``40``

  """

  return int( trophy.find( 'span', { 'class' : 'contentRow-figure contentRow-figure--text contentRow-figure--fixedSmall' } ).text )

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

def get_trophy_name( trophy ):

  """Get the name of a user's trophy, from BeautifulSoup of HTML snippet
  containing information for one trophy

  Parameters
  ----------
  trophy : bs4.element.Tag
    BeautifulSoup of HTML snippet that contains information for one trophy

  Returns
  -------
  str
    Name of trophy
    e.g. ``'Talent Finder'``

  """

  return trophy.find( 'h2', { 'class' :  'contentRow-header' } ).text

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

def get_trophy_description( trophy ):

  """Get the description of a user's trophy, from BeautifulSoup of HTML snippet
  containing information for one trophy

  Parameters
  ----------
  trophy : bs4.element.Tag
    BeautifulSoup of HTML snippet that contains information for one trophy

  Returns
  -------
  str
    Description of trophy
    e.g. ``'Create a Lolcow thread that receives over 100,000 views.'``

  """

  return trophy.find( 'div', { 'class' : 'contentRow-minor' } ).text

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

def get_trophy_time( trophy ):

  """Get the timestamp of a user's trophy, from BeautifulSoup of HTML snippet
  containing information for one trophy

  Parameters
  ----------
  trophy : bs4.element.Tag
    BeautifulSoup of HTML snippet that contains information for one trophy

  Returns
  -------
  int
    Timestamp of trophy
    e.g. ``1443429463``

  """

  return int( trophy.find( 'time', { 'class' : 'u-dt' } )[ 'data-time' ] )

###############################################################################