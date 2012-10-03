NEWS
====

v0.3.3 -- 2012-06-06
--------------------

:Version name: FlyingRazorback

* Graphical interface
    * Visualization and encoding filters
    * Mathematical filters (Base64, GZIP, BZ2)
    * Dedicated Search View
    * Preview of data rendering in contextual menu
    * Support format visualization at the symbol level
* Partitioning
    * Alignment and sequencing by field
    * Execute alignment on specified symbols
    * Split field by the right
    * Allow the partitioning of messages with specified boundaries
    * Allow partitioning at the project and symbol level
    * Similarity score based on number of common dynamic elements
    * Optimization of Needleman : don't repeat the same computation twice
    * Implement native UPGMA algorithm
* Grammar inference
    * Infer the grammar of a network client
* Project/trace management
    * Export / Import projects
    * Importer for XML formated traces

v0.3.2 -- 2012-02-23
--------------------

* Upgrade Vocabulary Inference
    * Add Octal visualization
        * Feature #57: Resize columns
        * Feature #59: Allows to copy message/field to clipboard
        * Feature #60: Support simple alignment
        * Feature #62: Allow the deletion of multiple messages at a time
        * Feature #20: Show the current status of an alignment
        * Manual modification of the Regex of a field		
    * Upgrade Grammar Inference
        * Feature #55: Dedicated GUI for the automatic inferring process
    * Upgrade Simulator
        * Feature #87: Specify source port for network simulator
* Upgrade Import/Export and Traces Management
    * Feature #22: Activate the management of traces
    * Feature #61: Traces must be compressed when stored in the trace manager
    * Feature #92: Handle cooked socket (SLL) packet format
    * Feature #83: Support of human readable format export
    * Support Unicode for filenames
* Extra
    * Workspace can be specified through a command line argument
    * Feature #73: Add manpage for Netzob
    * Feature #74: Add ".desktop" file in the official version
    * Apply pep8 quality repository on source code
    	
v0.3.1 -- 2012-01-12
--------------------

* Small fixes

v0.3 -- 2012-01-12
------------------

* Upgraded GUI and user experience
    * Add a menu
    * Simplify the Vocabulary inference panel
    * Add Workspaces and Projects definitions
* Upgrade Vocabulary Inference
    * Add alignment based on an arbitrary delimitor
    * Identification of the definition domain of a field
    * Add support for environmental dependencies
    * Add new visualization of data encoding
        * Format: hex, string and binary
        * Unit size: bit, 8-bits, 16-bits, 32-bits and 64-bits
        * Sign: signed and unsigned
        * Endianess: big and little endian
    * Add concept of variable :
        * Include Binary Value
        * Include Word Value
        * Include Aggregate Value
        * Include Alternate Value
* Add grammar inference module
    * Add the definition of the MMSTD model
    * Implementation of the Angluin L* algorithm
    * Implementation of the W-Method Algorithm
    * Add an alpha version of the automatic inferring process
* Add simulation module 
    * Supports Network Server and Client simulations
* Add import modules : files and library calls
    * Add multiple files import
* Extra
    * SVN to GIT migration
    * Dedicated website (http://www.netzob.org)

v0.2 -- 2011-09-01
------------------

* Add import modules : IPC, PCAP and Live network flows
* Add export module : raw XML format
* Improvement of Needleman and Wunsh performance with OpenMP

v0.1 -- 2011-08-16
------------------

* Initial release