import pathlib
import argparse
import os
import platform
import subprocess

doxygen_configuration = """
DOXYFILE_ENCODING      = UTF-8
PROJECT_NAME           = {PROJECT_NAME}
PROJECT_NUMBER         =
PROJECT_BRIEF          =
PROJECT_LOGO           =
OUTPUT_DIRECTORY       = {DESTINATION_PATH}
CREATE_SUBDIRS         = NO
ALLOW_UNICODE_NAMES    = NO
OUTPUT_LANGUAGE        = English
OUTPUT_TEXT_DIRECTION  = None
BRIEF_MEMBER_DESC      = YES
REPEAT_BRIEF           = YES
ABBREVIATE_BRIEF       = "The $name class" \\
                         "The $name widget" \\
                         "The $name file" \\
                         is \\
                         provides \\
                         specifies \\
                         contains \\
                         represents \\
                         a \\
                         an \\
                         the
ALWAYS_DETAILED_SEC    = NO
INLINE_INHERITED_MEMB  = NO
FULL_PATH_NAMES        = YES
STRIP_FROM_PATH        =
STRIP_FROM_INC_PATH    =
SHORT_NAMES            = NO
JAVADOC_AUTOBRIEF      = NO
JAVADOC_BANNER         = NO
QT_AUTOBRIEF           = NO
MULTILINE_CPP_IS_BRIEF = NO
PYTHON_DOCSTRING       = YES
INHERIT_DOCS           = YES
SEPARATE_MEMBER_PAGES  = NO
TAB_SIZE               = 4
ALIASES                =
OPTIMIZE_OUTPUT_FOR_C  = NO
OPTIMIZE_OUTPUT_JAVA   = NO
OPTIMIZE_FOR_FORTRAN   = NO
OPTIMIZE_OUTPUT_VHDL   = NO
OPTIMIZE_OUTPUT_SLICE  = NO
EXTENSION_MAPPING      =
MARKDOWN_SUPPORT       = YES
TOC_INCLUDE_HEADINGS   = 5
AUTOLINK_SUPPORT       = YES
BUILTIN_STL_SUPPORT    = NO
CPP_CLI_SUPPORT        = NO
SIP_SUPPORT            = NO
IDL_PROPERTY_SUPPORT   = YES
DISTRIBUTE_GROUP_DOC   = NO
GROUP_NESTED_COMPOUNDS = NO
SUBGROUPING            = YES
INLINE_GROUPED_CLASSES = NO
INLINE_SIMPLE_STRUCTS  = NO
TYPEDEF_HIDES_STRUCT   = NO
LOOKUP_CACHE_SIZE      = 0
NUM_PROC_THREADS       = 1
EXTRACT_ALL            = YES
EXTRACT_PRIVATE        = NO
EXTRACT_PRIV_VIRTUAL   = NO
EXTRACT_PACKAGE        = NO
EXTRACT_STATIC         = NO
EXTRACT_LOCAL_CLASSES  = YES
EXTRACT_LOCAL_METHODS  = NO
EXTRACT_ANON_NSPACES   = NO
RESOLVE_UNNAMED_PARAMS = YES
HIDE_UNDOC_MEMBERS     = NO
HIDE_UNDOC_CLASSES     = NO
HIDE_FRIEND_COMPOUNDS  = NO
HIDE_IN_BODY_DOCS      = NO
INTERNAL_DOCS          = NO
CASE_SENSE_NAMES       = NO
HIDE_SCOPE_NAMES       = NO
HIDE_COMPOUND_REFERENCE= NO
SHOW_INCLUDE_FILES     = YES
SHOW_GROUPED_MEMB_INC  = NO
FORCE_LOCAL_INCLUDES   = NO
INLINE_INFO            = YES
SORT_MEMBER_DOCS       = YES
SORT_BRIEF_DOCS        = NO
SORT_MEMBERS_CTORS_1ST = NO
SORT_GROUP_NAMES       = NO
SORT_BY_SCOPE_NAME     = NO
STRICT_PROTO_MATCHING  = NO
GENERATE_TODOLIST      = YES
GENERATE_TESTLIST      = YES
GENERATE_BUGLIST       = YES
GENERATE_DEPRECATEDLIST= YES
ENABLED_SECTIONS       =
MAX_INITIALIZER_LINES  = 30
SHOW_USED_FILES        = YES
SHOW_FILES             = YES
SHOW_NAMESPACES        = YES
FILE_VERSION_FILTER    =
LAYOUT_FILE            =
CITE_BIB_FILES         =
QUIET                  = NO
WARNINGS               = YES
WARN_IF_UNDOCUMENTED   = YES
WARN_IF_DOC_ERROR      = YES
WARN_NO_PARAMDOC       = NO
WARN_AS_ERROR          = NO
WARN_FORMAT            = "$file:$line: $text"
WARN_LOGFILE           =
INPUT                  = {SOURCE_PATH}
INPUT_ENCODING         = UTF-8
FILE_PATTERNS          = *.c \\
                         *.cc \\
                         *.cxx \\
                         *.cpp \\
                         *.c++ \\
                         *.java \\
                         *.ii \\
                         *.ixx \\
                         *.ipp \\
                         *.i++ \\
                         *.inl \\
                         *.idl \\
                         *.ddl \\
                         *.odl \\
                         *.h \\
                         *.hh \\
                         *.hxx \\
                         *.hpp \\
                         *.h++ \\
                         *.cs \\
                         *.d \\
                         *.php \\
                         *.php4 \\
                         *.php5 \\
                         *.phtml \\
                         *.inc \\
                         *.m \\
                         *.markdown \\
                         *.md \\
                         *.mm \\
                         *.dox \\
                         *.py \\
                         *.pyw \\
                         *.f90 \\
                         *.f95 \\
                         *.f03 \\
                         *.f08 \\
                         *.f18 \\
                         *.f \\
                         *.for \\
                         *.vhd \\
                         *.vhdl \\
                         *.ucf \\
                         *.qsf \\
                         *.ice
RECURSIVE              = YES
EXCLUDE                = {EXCLUDE_PATHS}
EXCLUDE_SYMLINKS       = NO
EXCLUDE_PATTERNS       =
EXCLUDE_SYMBOLS        =
EXAMPLE_PATH           =
EXAMPLE_PATTERNS       = *
EXAMPLE_RECURSIVE      = NO
IMAGE_PATH             =
INPUT_FILTER           =
FILTER_PATTERNS        =
FILTER_SOURCE_FILES    = NO
FILTER_SOURCE_PATTERNS =
USE_MDFILE_AS_MAINPAGE =
SOURCE_BROWSER         = NO
INLINE_SOURCES         = NO
STRIP_CODE_COMMENTS    = YES
REFERENCED_BY_RELATION = NO
REFERENCES_RELATION    = NO
REFERENCES_LINK_SOURCE = YES
SOURCE_TOOLTIPS        = YES
USE_HTAGS              = NO
VERBATIM_HEADERS       = YES
CLANG_ASSISTED_PARSING = NO
CLANG_ADD_INC_PATHS    = YES
CLANG_OPTIONS          =
CLANG_DATABASE_PATH    =
ALPHABETICAL_INDEX     = YES
IGNORE_PREFIX          =
GENERATE_HTML          = YES
HTML_OUTPUT            = html
HTML_FILE_EXTENSION    = .html
HTML_HEADER            =
HTML_FOOTER            =
HTML_STYLESHEET        =
HTML_EXTRA_STYLESHEET  =
HTML_EXTRA_FILES       =
HTML_COLORSTYLE_HUE    = 220
HTML_COLORSTYLE_SAT    = 100
HTML_COLORSTYLE_GAMMA  = 80
HTML_TIMESTAMP         = NO
HTML_DYNAMIC_MENUS     = YES
HTML_DYNAMIC_SECTIONS  = NO
HTML_INDEX_NUM_ENTRIES = 100
GENERATE_DOCSET        = NO
DOCSET_FEEDNAME        = "Doxygen generated docs"
DOCSET_BUNDLE_ID       = org.doxygen.Project
DOCSET_PUBLISHER_ID    = org.doxygen.Publisher
DOCSET_PUBLISHER_NAME  = Publisher
GENERATE_HTMLHELP      = NO
CHM_FILE               =
HHC_LOCATION           =
GENERATE_CHI           = NO
CHM_INDEX_ENCODING     =
BINARY_TOC             = NO
TOC_EXPAND             = NO
GENERATE_QHP           = NO
QCH_FILE               =
QHP_NAMESPACE          = org.doxygen.Project
QHP_VIRTUAL_FOLDER     = doc
QHP_CUST_FILTER_NAME   =
QHP_CUST_FILTER_ATTRS  =
QHP_SECT_FILTER_ATTRS  =
QHG_LOCATION           =
GENERATE_ECLIPSEHELP   = NO
ECLIPSE_DOC_ID         = org.doxygen.Project
DISABLE_INDEX          = NO
GENERATE_TREEVIEW      = YES
ENUM_VALUES_PER_LINE   = 4
TREEVIEW_WIDTH         = 250
EXT_LINKS_IN_WINDOW    = NO
HTML_FORMULA_FORMAT    = png
FORMULA_FONTSIZE       = 10
FORMULA_TRANSPARENT    = YES
FORMULA_MACROFILE      =
USE_MATHJAX            = NO
MATHJAX_FORMAT         = HTML-CSS
MATHJAX_RELPATH        = https://cdn.jsdelivr.net/npm/mathjax@2
MATHJAX_EXTENSIONS     =
MATHJAX_CODEFILE       =
SEARCHENGINE           = YES
SERVER_BASED_SEARCH    = NO
EXTERNAL_SEARCH        = NO
SEARCHENGINE_URL       =
SEARCHDATA_FILE        = searchdata.xml
EXTERNAL_SEARCH_ID     =
EXTRA_SEARCH_MAPPINGS  =
GENERATE_LATEX         = NO
LATEX_OUTPUT           = latex
LATEX_CMD_NAME         =
MAKEINDEX_CMD_NAME     = makeindex
LATEX_MAKEINDEX_CMD    = makeindex
COMPACT_LATEX          = NO
PAPER_TYPE             = a4
EXTRA_PACKAGES         =
LATEX_HEADER           =
LATEX_FOOTER           =
LATEX_EXTRA_STYLESHEET =
LATEX_EXTRA_FILES      =
PDF_HYPERLINKS         = YES
USE_PDFLATEX           = YES
LATEX_BATCHMODE        = NO
LATEX_HIDE_INDICES     = NO
LATEX_SOURCE_CODE      = NO
LATEX_BIB_STYLE        = plain
LATEX_TIMESTAMP        = NO
LATEX_EMOJI_DIRECTORY  =
GENERATE_RTF           = NO
RTF_OUTPUT             = rtf
COMPACT_RTF            = NO
RTF_HYPERLINKS         = NO
RTF_STYLESHEET_FILE    =
RTF_EXTENSIONS_FILE    =
RTF_SOURCE_CODE        = NO
GENERATE_MAN           = NO
MAN_OUTPUT             = man
MAN_EXTENSION          = .3
MAN_SUBDIR             =
MAN_LINKS              = NO
GENERATE_XML           = NO
XML_OUTPUT             = xml
XML_PROGRAMLISTING     = YES
XML_NS_MEMB_FILE_SCOPE = NO
GENERATE_DOCBOOK       = NO
DOCBOOK_OUTPUT         = docbook
DOCBOOK_PROGRAMLISTING = NO
GENERATE_AUTOGEN_DEF   = NO
GENERATE_PERLMOD       = NO
PERLMOD_LATEX          = NO
PERLMOD_PRETTY         = YES
PERLMOD_MAKEVAR_PREFIX =
ENABLE_PREPROCESSING   = YES
MACRO_EXPANSION        = NO
EXPAND_ONLY_PREDEF     = NO
SEARCH_INCLUDES        = YES
INCLUDE_PATH           =
INCLUDE_FILE_PATTERNS  =
PREDEFINED             =
EXPAND_AS_DEFINED      =
SKIP_FUNCTION_MACROS   = YES
TAGFILES               =
GENERATE_TAGFILE       =
ALLEXTERNALS           = NO
EXTERNAL_GROUPS        = YES
EXTERNAL_PAGES         = YES
CLASS_DIAGRAMS         = YES
DIA_PATH               =
HIDE_UNDOC_RELATIONS   = YES
HAVE_DOT               = YES
DOT_NUM_THREADS        = 0
DOT_FONTNAME           = Helvetica
DOT_FONTSIZE           = 10
DOT_FONTPATH           =
CLASS_GRAPH            = YES
COLLABORATION_GRAPH    = YES
GROUP_GRAPHS           = YES
UML_LOOK               = YES
UML_LIMIT_NUM_FIELDS   = 20
DOT_UML_DETAILS        = NO
DOT_WRAP_THRESHOLD     = 17
TEMPLATE_RELATIONS     = NO
INCLUDE_GRAPH          = YES
INCLUDED_BY_GRAPH      = YES
CALL_GRAPH             = YES
CALLER_GRAPH           = YES
GRAPHICAL_HIERARCHY    = YES
DIRECTORY_GRAPH        = YES
DOT_IMAGE_FORMAT       = png
INTERACTIVE_SVG        = NO
DOT_PATH               =
DOTFILE_DIRS           =
MSCFILE_DIRS           =
DIAFILE_DIRS           =
PLANTUML_JAR_PATH      =
PLANTUML_CFG_FILE      =
PLANTUML_INCLUDE_PATH  =
DOT_GRAPH_MAX_NODES    = 50
MAX_DOT_GRAPH_DEPTH    = 0
DOT_TRANSPARENT        = NO
DOT_MULTI_TARGETS      = NO
GENERATE_LEGEND        = YES
DOT_CLEANUP            = YES
"""


# Utility functions
# ------------------------------------------------------------------------------


def IsProgramInstalled(program):
    if not "/usr/" in subprocess.getoutput("whereis {program}".format(program=program)):
        print("The \"{program}\" is not installed".format(program=program))
        return False

    return True


def CreateFolder(destination_path):
    result_path = pathlib.Path(destination_path)
    result_path.mkdir(parents=True, exist_ok=True)


def ConvertListToDoxygenList(list_with_data):
    if len(list_with_data) == 0:
        return ""

    if len(list_with_data) == 1:
        return str(list_with_data[0])
    else:
        result = ""

        for item in list_with_data:
            result += item + " \\" + "\n"

        # Removing excess ' \\n' symbols for the last line
        result = result[:-3]

        return result


def GetLastSectionInPath(source):
    return source[source.rfind("/"):]


# Doxydoc functions
# ------------------------------------------------------------------------------


def ValidateRequiredPackagesInstalled():
    result = True

    # TODO: Support Windows
    if platform.system() == "Windows":
        return result

    if not IsProgramInstalled("doxygen"):
        result = False
    if not IsProgramInstalled("graphviz"):
        result = False

    return result


def CreateArgumentParser():
    parser = argparse.ArgumentParser(
        description="""
        This generator is aimed to create Doxygen documentation with call-by/
        called-by graphs and UML diagrams.
        "doxygen" & "graphviz" packages must be installed. To install them do
        the following: "sudo apt install -y doxygen graphviz".
        After script executed navigate to the destinanion folder and open
        /html/index.html via any browser you prefer.
        """
    )

    parser.add_argument(
        "-s",
        "--source",
        action="store",
        required=True,
        help="""
        Uses for indicating the source code folder from where Doxygen
        generation starts.
        """
    )
    parser.add_argument(
        "-d",
        "--destination",
        action="store",
        help="""
        Uses for indicating the destination folder to where Doxygen
        generation puts the result. By default it is the current working dir.
        """
    )
    parser.add_argument(
        "-e",
        "--exclude",
        nargs="*",
        help="""
        Uses for indicating folder(s) relatively to <source> that should not be
        involved in Doxygen generation.
        """
    )

    return parser


def CreateDestinationFolder(source_path, destination_path):
    if not destination_path:
        destination_path = os.getcwd()

    result_folder_name = GetLastSectionInPath(source_path)
    destination_path += result_folder_name

    CreateFolder(destination_path)

    return destination_path


def ValidateUserInput(source_path, destination_path, exclude_paths_list):
    result = True

    if not source_path:
        print(
            "Invalid value for \"source\" parameter: {sp}".format(sp=source_path)
        )
        result = False
    if not destination_path:
        print(
            "Invalid value for \"destination\" parameter: {dp}".format(dp=destination_path)
        )
        result = False

    if not os.path.isdir(source_path):
        print(
            "No directory exists for \"source\" parameter: {sp}".format(sp=source_path)
        )
        result = False
    if not os.path.isdir(destination_path):
        print(
            "No directory exists for \"destination\" parameter: {dp}".format(dp=destination_path)
        )

    if exclude_paths_list:
          for exclude_path in exclude_paths_list:
              if not os.path.isdir(exclude_path):
                  print(
                      "No directory exists for \"exclude\" value: {ep}".format(ep=exclude_path)
                  )
                  result = False

    return result


def ConfigureDoxygen(source_path, destination_path, exclude_paths_list):
    configuration = doxygen_configuration

    configuration = configuration.replace("{SOURCE_PATH}", source_path)
    configuration = configuration.replace("{DESTINATION_PATH}", destination_path)
    configuration = configuration.replace("{PROJECT_NAME}", GetLastSectionInPath(source_path))

    if exclude_paths_list:
        configuration = configuration.replace(
            "{EXCLUDE_PATHS}",
            ConvertListToDoxygenList(exclude_paths_list)
        )

    return configuration


def RunDoxygen(configuration):
    doxygen_conf_user_file_path = os.getcwd() + "doxygen.conf.user"

    resultFile = open(doxygen_conf_user_file_path, 'w')
    resultFile.write(configuration)
    resultFile.close()

    subprocess.run(["doxygen", doxygen_conf_user_file_path])
    os.remove(doxygen_conf_user_file_path)


# Main function
# ------------------------------------------------------------------------------


if __name__ == '__main__':

    if not ValidateRequiredPackagesInstalled():
        os.sys.exit('Not all required packages are present')

    parser = CreateArgumentParser()
    args = parser.parse_args()

    source_path = args.source
    destination_path = args.destination
    exclude_paths_list = args.exclude

    if "/" not in source_path:
        source_path = "~/" + source_path

    destination_path = CreateDestinationFolder(source_path, destination_path)

    if exclude_paths_list:
        abs_exclude_paths_list = []
        # NOTE: Due to doxygen claims absolute paths for exclusion it is required to convert
        # user's relative paths to absolute ones.
        abs_path_of_source_dir = os.path.abspath(source_path)

        for exclude_path in exclude_paths_list:
            abs_exclude_paths_list.append(abs_path_of_source_dir + "/" + exclude_path)

        exclude_paths_list = abs_exclude_paths_list

    if not ValidateUserInput(source_path, destination_path, exclude_paths_list):
        os.sys.exit('Not valid user input')

    configuration = ConfigureDoxygen(source_path, destination_path, exclude_paths_list)
    RunDoxygen(configuration)