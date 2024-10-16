AUTHOR = 'TSSC'
SITEURL = ""
SITELOGO_SIZE = 32
SITEURL = "https://heasarc.gsfc.nasa.gov/docs/tess"	
FULLURL = "https://heasarc.gsfc.nasa.gov/docs/tess"

PATH = "content"
STATIC_PATHS = ['images','data','docs']
SITELOGO = 'images/logos/NASA_logo_vector_lg.png'

TIMEZONE = 'US/Eastern'

DEFAULT_LANG = 'en'

SITENAME = 'TESS'
HIDE_SITENAME = False

THEME = "themes/pelican-bootstrap3-tess"
#CSS_FILE = "themes/pelican-bootstrap3-tess/static"
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
BOOTSTRAP_THEME = 'cerulean'
BOOTSTRAP_FLUID = False
FAVICON = 'images/logos/favicon.png'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

#Value for the front page counter 
from datetime import date
SCIENCE_DAYS = (date.today() - date.fromisoformat('2018-07-18')).days

PLUGINS = [
    # list of plugins I have enabled
    'autoloader',                                                                                                           
    'i18n_subsites',                                                                                                           
    'jinja2content',                                                                                                        
    'jinja_filters',                                                                                                                                                                                                               
    'photos',                                                                                                          
    'render_math',                                                                                                  
    'theme_config',
    #'search',
    'md_include',
]



# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

#STORK_INPUT_OPTIONS = {
#    base_directory == PATH
#}

# Social widget
#SOCIAL = (
#    ("You can add links in your config file", "#"),
#    ("Another social link", "#"),
#)

IGNORE_FILES = [
    "README.md","make_static_plots.py", "make-approved-programs.py", "tpub.db"
]

MD_INCLUDE_BASE_PATH = 'htmlcontent'
'''MARKDOWN = {
  'extension_configs': {
    'markdown.extensions.toc': {},
    'md_include': {
            'base_path': "htmlcontent",
            'allow_local': True,
            'allow_remote': True,
            'recurs_local': True,
            'recurs_remote': True
        }
  }
}'''

SHOW_ARTICLE_AUTHOR = True
DEFAULT_PAGINATION = 5

RELATIVE_URLS = True
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = True
DISPLAY_ARTICLE_INFO_ON_INDEX = True



MENUITEMS = (
          ('Education Resources', (
            ('What is TESS?', 'what-is-tess.html'),
            ('TESS Statistics', 'statistics.html'),
            ('Citizen Science', 'citizen_science.html'),
            ('Outreach Materials', 'outreach.html'),
                    )
        ),

        ('Science Resources', (
            #('TESS Statistics', 'statistics.html'),
            ('Telescope Information', 'telescope_information.html'),
            ('Sector Information', 'sector.html'),
            #('TESS Data', 'data_pipeline.html'),
            ('Data Products', 'data_products.html'),
            ('Follow-up Program', 'tfop.html'),
            ('Users Committee', 'tuc.html'),
            ('Media Requests', 'mediarequest.html'),
            ('FAQ', 'faq.html'),
            ('Documentation Resources', 'documentation.html'),
             )
        ),
        ('Tools and Tutorials', (
            ('Tutorials', 'tutorial_landing.html'),
            ('Data Analysis Tools', 'community.html'),
            ('Proposal Tools', 'proposing_tools.html'),
            ('TESS-point Web Tool', 'https://heasarc.gsfc.nasa.gov/wsgi-scripts/TESS/TESS-point_Web_Tool/TESS-point_Web_Tool/wtv_v2.0.py'), #'tesspoint.html'),
            #('Work with TESS Data online with TiKE', 'new_proposing.html'),
                    )
        ),
        ('Propose for Observations', (
            ('How to Propose', 'proposing.html'),
            ('Previous Approved Programs', 'approved-programs.html'),
            ('Director\'s Discretionary Targets', 'ddt.html')
                    )
        ),

        #('Tutorials', (
            #('TESS tutorials', 'tutorial_landing.html'),
            #('FAQ', 'faq.html'),
            #('Tutorial 1', 'tutorial1.html'),
            #('Tutorial 2', 'tutorial2.html'),
            #('Tutorial 3', 'new_proposing.html'),
                    #)
        #),

        )