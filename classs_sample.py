#!/usr/bin/python3

""" This script is a template with an empty class and __main__ for any Python scripts.

    Great example of the following concepts:
    - Has a 'main' using the class, so the class functionality can be imported on it's own or be used by a direct call into the script.
    - uses 'argparse' to parse parameters.
    - Class has '__init__' member (constructor)
    - My usual 'trace' class member to extend the verbose into the class.
    - A member function shows how to call a sub-process.]
    - A member function shows how to call a sub-process, redirecting the output to a log file.

   
    # import a class from another script using:
    from <file_no_extension> import <class>
    
    Tips:
    
    // Path join:
    os.path.join( "1", "2, "3 );
    
    // Reg-Ex for a string in a file :
    import re # Reg-ex module for our error search
    grep_for_build_error = ".*(c|cpp|h|hpp):[0-9]: Error" // May nolt be valid for gcc
    for line in log_file:
    if re.search( grep_for_error_string, line ):
        sys.stdout.write( line )
        nb_errors += 1
        
"""

import argparse
import os
import sys

from datetime import datetime


# Add utility to search and count unit-tests results



# Use this class to scan specific folder for unit-test result files, 
# accumulate statistics and print a report.
class my_template:

    # if True the class does additional 'print' - Use this in Verbose mode.
    trace_on = False
    current_folder = ""
    

    def __init__( self, verbose ):
        # Init each instance, or they all share the same list.
        self.trace_on = verbose
        current_folder = os.getcwd()
        self.trace( "Current folder: " + current_folder )

    # Debug utility - display a message if trace is enabled.
    def trace( self, message ) :
        if self.trace_on == True:
            print( message )


    def do_some_work( self, text ):
        self.trace( "I am verbose: let's do some work...")
        print( text )

    # start a sub-process
    def StartSubprocess( self, process, args ):
        self.trace( " About to call process: " + process + " from folder: current_folder" )
        
        # Setup the call to process with wanted parameters:
        process_params = [
            process, 
            "-r", "your_r_option", 
            "-f", "your_f_option",
            ]

        # Add any extra parameters received from the user
        trace( "Adding parameters to subprocess: " + str( args ) )
        for extra_args in args: 
            process_params.append( extra_args )
        
        p = subprocess.Popen( process_params, cwd=current_folder )
        p.wait()

        
    # start a sub-process redirecting all output to a specified log file
    def StartSubprocessResultInFile( self, process, args, log_file ):
        self.trace( " About to call process: " + process + " from folder: " + current_folder + " redirecting process output to " + log_file )
        
        # Setup the call to process with wanted paraneters:
        process_params = [
            process, 
            "-a", "your_a_option", 
            "-b", "your_b_option",
            ]

        # Add any extra parameters received from the user
        trace( "Adding parameters to subprocess: " + str( args ) )
        for extra_args in args: 
            process_params.append( extra_args )
              
        result_output = open( log_file, 'w' );
        result_output.write( "\n\n -- NEW CALL -- \n\n" ) # Send a few CR in the log file for readability of 'tail -f'.        
        if( self.trace_on ):
            result_output( "Calling: " + process_params + "\n" )
        result_output.flush()
            
        print( "Calling process: " + process + " follow the output using: " )
        print( "tail -F " + log_file )
        p = subprocess.Popen( process_params, cwd=self.local_root, stdout=result_output, stderr=result_output )
        p.wait()
    
# - END - of class


# - Scrip - work starts here
# --------------------------

# First we parse any received argument
# ex: my_script -v -a zibudi
arg_parser = argparse.ArgumentParser( description = "This is a template script for future use." )
arg_parser.add_argument( "-v", "--verbose", help = "Script outputs extra information on the work being done.", required = False, action='store_true' )
arg_parser.add_argument( "-a", "--automated", help = "Dummy parameter as a data storing sample.", required = False )

# Parse the received args.
arguments = arg_parser.parse_args()

# OR to get extra ergs i.e.: To pass extra arguments to a called sub-process: 
# args, extra_args = arg_parser.parse_known_args()

if __name__ == "__main__":

    # We want to know how long it takes to run this script...
    startTime = datetime.now()

    # Instanciate the worker class
    worker = my_template( arguments.verbose )
    
    print( "Starting work..." )
    worker.do_some_work( "This is work." )
    
    # Sample: how to use an argument with attached data.
    if( arguments.automated is not None ):
        worker.do_some_work( "Received --automated: " +  arguments.automated )
    else:
        worker.do_some_work( "Parameter --automated is empty." )

    # Print how long this script ran for.
    print( "---- " + os.path.basename(__file__) + " ran in " + str( datetime.now() - startTime ) + " ---" )
    
    print( " - That's all folks... -" )

