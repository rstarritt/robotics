# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.14

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/rstarritt/Documents/CSCI473/AstraSDK-v2.0.15-232757cc1d-20190327T080423Z-Linux/samples

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/rstarritt/Documents/CSCI473/AstraSDK-v2.0.15-232757cc1d-20190327T080423Z-Linux/samples

# Include any dependencies generated for this target.
include c-api/InfraredReaderPoll/CMakeFiles/InfraredReaderPoll.dir/depend.make

# Include the progress variables for this target.
include c-api/InfraredReaderPoll/CMakeFiles/InfraredReaderPoll.dir/progress.make

# Include the compile flags for this target's objects.
include c-api/InfraredReaderPoll/CMakeFiles/InfraredReaderPoll.dir/flags.make

c-api/InfraredReaderPoll/CMakeFiles/InfraredReaderPoll.dir/main.c.o: c-api/InfraredReaderPoll/CMakeFiles/InfraredReaderPoll.dir/flags.make
c-api/InfraredReaderPoll/CMakeFiles/InfraredReaderPoll.dir/main.c.o: c-api/InfraredReaderPoll/main.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/rstarritt/Documents/CSCI473/AstraSDK-v2.0.15-232757cc1d-20190327T080423Z-Linux/samples/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object c-api/InfraredReaderPoll/CMakeFiles/InfraredReaderPoll.dir/main.c.o"
	cd /home/rstarritt/Documents/CSCI473/AstraSDK-v2.0.15-232757cc1d-20190327T080423Z-Linux/samples/c-api/InfraredReaderPoll && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/InfraredReaderPoll.dir/main.c.o   -c /home/rstarritt/Documents/CSCI473/AstraSDK-v2.0.15-232757cc1d-20190327T080423Z-Linux/samples/c-api/InfraredReaderPoll/main.c

c-api/InfraredReaderPoll/CMakeFiles/InfraredReaderPoll.dir/main.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/InfraredReaderPoll.dir/main.c.i"
	cd /home/rstarritt/Documents/CSCI473/AstraSDK-v2.0.15-232757cc1d-20190327T080423Z-Linux/samples/c-api/InfraredReaderPoll && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/rstarritt/Documents/CSCI473/AstraSDK-v2.0.15-232757cc1d-20190327T080423Z-Linux/samples/c-api/InfraredReaderPoll/main.c > CMakeFiles/InfraredReaderPoll.dir/main.c.i

c-api/InfraredReaderPoll/CMakeFiles/InfraredReaderPoll.dir/main.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/InfraredReaderPoll.dir/main.c.s"
	cd /home/rstarritt/Documents/CSCI473/AstraSDK-v2.0.15-232757cc1d-20190327T080423Z-Linux/samples/c-api/InfraredReaderPoll && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/rstarritt/Documents/CSCI473/AstraSDK-v2.0.15-232757cc1d-20190327T080423Z-Linux/samples/c-api/InfraredReaderPoll/main.c -o CMakeFiles/InfraredReaderPoll.dir/main.c.s

# Object files for target InfraredReaderPoll
InfraredReaderPoll_OBJECTS = \
"CMakeFiles/InfraredReaderPoll.dir/main.c.o"

# External object files for target InfraredReaderPoll
InfraredReaderPoll_EXTERNAL_OBJECTS =

bin/InfraredReaderPoll: c-api/InfraredReaderPoll/CMakeFiles/InfraredReaderPoll.dir/main.c.o
bin/InfraredReaderPoll: c-api/InfraredReaderPoll/CMakeFiles/InfraredReaderPoll.dir/build.make
bin/InfraredReaderPoll: /home/rstarritt/Documents/CSCI473/AstraSDK-v2.0.15-232757cc1d-20190327T080423Z-Linux/lib/libastra_core.so
bin/InfraredReaderPoll: /home/rstarritt/Documents/CSCI473/AstraSDK-v2.0.15-232757cc1d-20190327T080423Z-Linux/lib/libastra_core_api.so
bin/InfraredReaderPoll: /home/rstarritt/Documents/CSCI473/AstraSDK-v2.0.15-232757cc1d-20190327T080423Z-Linux/lib/libastra.so
bin/InfraredReaderPoll: c-api/InfraredReaderPoll/CMakeFiles/InfraredReaderPoll.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/rstarritt/Documents/CSCI473/AstraSDK-v2.0.15-232757cc1d-20190327T080423Z-Linux/samples/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking C executable ../../bin/InfraredReaderPoll"
	cd /home/rstarritt/Documents/CSCI473/AstraSDK-v2.0.15-232757cc1d-20190327T080423Z-Linux/samples/c-api/InfraredReaderPoll && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/InfraredReaderPoll.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
c-api/InfraredReaderPoll/CMakeFiles/InfraredReaderPoll.dir/build: bin/InfraredReaderPoll

.PHONY : c-api/InfraredReaderPoll/CMakeFiles/InfraredReaderPoll.dir/build

c-api/InfraredReaderPoll/CMakeFiles/InfraredReaderPoll.dir/clean:
	cd /home/rstarritt/Documents/CSCI473/AstraSDK-v2.0.15-232757cc1d-20190327T080423Z-Linux/samples/c-api/InfraredReaderPoll && $(CMAKE_COMMAND) -P CMakeFiles/InfraredReaderPoll.dir/cmake_clean.cmake
.PHONY : c-api/InfraredReaderPoll/CMakeFiles/InfraredReaderPoll.dir/clean

c-api/InfraredReaderPoll/CMakeFiles/InfraredReaderPoll.dir/depend:
	cd /home/rstarritt/Documents/CSCI473/AstraSDK-v2.0.15-232757cc1d-20190327T080423Z-Linux/samples && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/rstarritt/Documents/CSCI473/AstraSDK-v2.0.15-232757cc1d-20190327T080423Z-Linux/samples /home/rstarritt/Documents/CSCI473/AstraSDK-v2.0.15-232757cc1d-20190327T080423Z-Linux/samples/c-api/InfraredReaderPoll /home/rstarritt/Documents/CSCI473/AstraSDK-v2.0.15-232757cc1d-20190327T080423Z-Linux/samples /home/rstarritt/Documents/CSCI473/AstraSDK-v2.0.15-232757cc1d-20190327T080423Z-Linux/samples/c-api/InfraredReaderPoll /home/rstarritt/Documents/CSCI473/AstraSDK-v2.0.15-232757cc1d-20190327T080423Z-Linux/samples/c-api/InfraredReaderPoll/CMakeFiles/InfraredReaderPoll.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : c-api/InfraredReaderPoll/CMakeFiles/InfraredReaderPoll.dir/depend

