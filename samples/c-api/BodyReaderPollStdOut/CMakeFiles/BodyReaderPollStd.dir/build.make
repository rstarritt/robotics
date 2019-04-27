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
CMAKE_SOURCE_DIR = /home/warfield/Code/robotics/samples

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/warfield/Code/robotics/samples

# Include any dependencies generated for this target.
include c-api/BodyReaderPollStdOut/CMakeFiles/BodyReaderPollStd.dir/depend.make

# Include the progress variables for this target.
include c-api/BodyReaderPollStdOut/CMakeFiles/BodyReaderPollStd.dir/progress.make

# Include the compile flags for this target's objects.
include c-api/BodyReaderPollStdOut/CMakeFiles/BodyReaderPollStd.dir/flags.make

c-api/BodyReaderPollStdOut/CMakeFiles/BodyReaderPollStd.dir/main.c.o: c-api/BodyReaderPollStdOut/CMakeFiles/BodyReaderPollStd.dir/flags.make
c-api/BodyReaderPollStdOut/CMakeFiles/BodyReaderPollStd.dir/main.c.o: c-api/BodyReaderPollStdOut/main.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/warfield/Code/robotics/samples/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object c-api/BodyReaderPollStdOut/CMakeFiles/BodyReaderPollStd.dir/main.c.o"
	cd /home/warfield/Code/robotics/samples/c-api/BodyReaderPollStdOut && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/BodyReaderPollStd.dir/main.c.o   -c /home/warfield/Code/robotics/samples/c-api/BodyReaderPollStdOut/main.c

c-api/BodyReaderPollStdOut/CMakeFiles/BodyReaderPollStd.dir/main.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/BodyReaderPollStd.dir/main.c.i"
	cd /home/warfield/Code/robotics/samples/c-api/BodyReaderPollStdOut && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/warfield/Code/robotics/samples/c-api/BodyReaderPollStdOut/main.c > CMakeFiles/BodyReaderPollStd.dir/main.c.i

c-api/BodyReaderPollStdOut/CMakeFiles/BodyReaderPollStd.dir/main.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/BodyReaderPollStd.dir/main.c.s"
	cd /home/warfield/Code/robotics/samples/c-api/BodyReaderPollStdOut && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/warfield/Code/robotics/samples/c-api/BodyReaderPollStdOut/main.c -o CMakeFiles/BodyReaderPollStd.dir/main.c.s

# Object files for target BodyReaderPollStd
BodyReaderPollStd_OBJECTS = \
"CMakeFiles/BodyReaderPollStd.dir/main.c.o"

# External object files for target BodyReaderPollStd
BodyReaderPollStd_EXTERNAL_OBJECTS =

bin/BodyReaderPollStd: c-api/BodyReaderPollStdOut/CMakeFiles/BodyReaderPollStd.dir/main.c.o
bin/BodyReaderPollStd: c-api/BodyReaderPollStdOut/CMakeFiles/BodyReaderPollStd.dir/build.make
bin/BodyReaderPollStd: /home/warfield/Code/robotics/lib/libastra_core.so
bin/BodyReaderPollStd: /home/warfield/Code/robotics/lib/libastra_core_api.so
bin/BodyReaderPollStd: /home/warfield/Code/robotics/lib/libastra.so
bin/BodyReaderPollStd: c-api/BodyReaderPollStdOut/CMakeFiles/BodyReaderPollStd.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/warfield/Code/robotics/samples/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking C executable ../../bin/BodyReaderPollStd"
	cd /home/warfield/Code/robotics/samples/c-api/BodyReaderPollStdOut && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/BodyReaderPollStd.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
c-api/BodyReaderPollStdOut/CMakeFiles/BodyReaderPollStd.dir/build: bin/BodyReaderPollStd

.PHONY : c-api/BodyReaderPollStdOut/CMakeFiles/BodyReaderPollStd.dir/build

c-api/BodyReaderPollStdOut/CMakeFiles/BodyReaderPollStd.dir/clean:
	cd /home/warfield/Code/robotics/samples/c-api/BodyReaderPollStdOut && $(CMAKE_COMMAND) -P CMakeFiles/BodyReaderPollStd.dir/cmake_clean.cmake
.PHONY : c-api/BodyReaderPollStdOut/CMakeFiles/BodyReaderPollStd.dir/clean

c-api/BodyReaderPollStdOut/CMakeFiles/BodyReaderPollStd.dir/depend:
	cd /home/warfield/Code/robotics/samples && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/warfield/Code/robotics/samples /home/warfield/Code/robotics/samples/c-api/BodyReaderPollStdOut /home/warfield/Code/robotics/samples /home/warfield/Code/robotics/samples/c-api/BodyReaderPollStdOut /home/warfield/Code/robotics/samples/c-api/BodyReaderPollStdOut/CMakeFiles/BodyReaderPollStd.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : c-api/BodyReaderPollStdOut/CMakeFiles/BodyReaderPollStd.dir/depend

