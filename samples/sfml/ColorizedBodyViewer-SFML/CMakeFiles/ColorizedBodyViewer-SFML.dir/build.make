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
include sfml/ColorizedBodyViewer-SFML/CMakeFiles/ColorizedBodyViewer-SFML.dir/depend.make

# Include the progress variables for this target.
include sfml/ColorizedBodyViewer-SFML/CMakeFiles/ColorizedBodyViewer-SFML.dir/progress.make

# Include the compile flags for this target's objects.
include sfml/ColorizedBodyViewer-SFML/CMakeFiles/ColorizedBodyViewer-SFML.dir/flags.make

sfml/ColorizedBodyViewer-SFML/CMakeFiles/ColorizedBodyViewer-SFML.dir/main.cpp.o: sfml/ColorizedBodyViewer-SFML/CMakeFiles/ColorizedBodyViewer-SFML.dir/flags.make
sfml/ColorizedBodyViewer-SFML/CMakeFiles/ColorizedBodyViewer-SFML.dir/main.cpp.o: sfml/ColorizedBodyViewer-SFML/main.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/rstarritt/Documents/CSCI473/AstraSDK-v2.0.15-232757cc1d-20190327T080423Z-Linux/samples/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object sfml/ColorizedBodyViewer-SFML/CMakeFiles/ColorizedBodyViewer-SFML.dir/main.cpp.o"
	cd /home/rstarritt/Documents/CSCI473/AstraSDK-v2.0.15-232757cc1d-20190327T080423Z-Linux/samples/sfml/ColorizedBodyViewer-SFML && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/ColorizedBodyViewer-SFML.dir/main.cpp.o -c /home/rstarritt/Documents/CSCI473/AstraSDK-v2.0.15-232757cc1d-20190327T080423Z-Linux/samples/sfml/ColorizedBodyViewer-SFML/main.cpp

sfml/ColorizedBodyViewer-SFML/CMakeFiles/ColorizedBodyViewer-SFML.dir/main.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/ColorizedBodyViewer-SFML.dir/main.cpp.i"
	cd /home/rstarritt/Documents/CSCI473/AstraSDK-v2.0.15-232757cc1d-20190327T080423Z-Linux/samples/sfml/ColorizedBodyViewer-SFML && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/rstarritt/Documents/CSCI473/AstraSDK-v2.0.15-232757cc1d-20190327T080423Z-Linux/samples/sfml/ColorizedBodyViewer-SFML/main.cpp > CMakeFiles/ColorizedBodyViewer-SFML.dir/main.cpp.i

sfml/ColorizedBodyViewer-SFML/CMakeFiles/ColorizedBodyViewer-SFML.dir/main.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/ColorizedBodyViewer-SFML.dir/main.cpp.s"
	cd /home/rstarritt/Documents/CSCI473/AstraSDK-v2.0.15-232757cc1d-20190327T080423Z-Linux/samples/sfml/ColorizedBodyViewer-SFML && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/rstarritt/Documents/CSCI473/AstraSDK-v2.0.15-232757cc1d-20190327T080423Z-Linux/samples/sfml/ColorizedBodyViewer-SFML/main.cpp -o CMakeFiles/ColorizedBodyViewer-SFML.dir/main.cpp.s

# Object files for target ColorizedBodyViewer-SFML
ColorizedBodyViewer__SFML_OBJECTS = \
"CMakeFiles/ColorizedBodyViewer-SFML.dir/main.cpp.o"

# External object files for target ColorizedBodyViewer-SFML
ColorizedBodyViewer__SFML_EXTERNAL_OBJECTS =

bin/ColorizedBodyViewer-SFML: sfml/ColorizedBodyViewer-SFML/CMakeFiles/ColorizedBodyViewer-SFML.dir/main.cpp.o
bin/ColorizedBodyViewer-SFML: sfml/ColorizedBodyViewer-SFML/CMakeFiles/ColorizedBodyViewer-SFML.dir/build.make
bin/ColorizedBodyViewer-SFML: /home/rstarritt/Documents/CSCI473/AstraSDK-v2.0.15-232757cc1d-20190327T080423Z-Linux/lib/libastra_core.so
bin/ColorizedBodyViewer-SFML: /home/rstarritt/Documents/CSCI473/AstraSDK-v2.0.15-232757cc1d-20190327T080423Z-Linux/lib/libastra_core_api.so
bin/ColorizedBodyViewer-SFML: /home/rstarritt/Documents/CSCI473/AstraSDK-v2.0.15-232757cc1d-20190327T080423Z-Linux/lib/libastra.so
bin/ColorizedBodyViewer-SFML: /usr/lib/libsfml-graphics.so
bin/ColorizedBodyViewer-SFML: /usr/lib/libsfml-window.so
bin/ColorizedBodyViewer-SFML: /usr/lib/libsfml-system.so
bin/ColorizedBodyViewer-SFML: sfml/ColorizedBodyViewer-SFML/CMakeFiles/ColorizedBodyViewer-SFML.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/rstarritt/Documents/CSCI473/AstraSDK-v2.0.15-232757cc1d-20190327T080423Z-Linux/samples/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable ../../bin/ColorizedBodyViewer-SFML"
	cd /home/rstarritt/Documents/CSCI473/AstraSDK-v2.0.15-232757cc1d-20190327T080423Z-Linux/samples/sfml/ColorizedBodyViewer-SFML && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/ColorizedBodyViewer-SFML.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
sfml/ColorizedBodyViewer-SFML/CMakeFiles/ColorizedBodyViewer-SFML.dir/build: bin/ColorizedBodyViewer-SFML

.PHONY : sfml/ColorizedBodyViewer-SFML/CMakeFiles/ColorizedBodyViewer-SFML.dir/build

sfml/ColorizedBodyViewer-SFML/CMakeFiles/ColorizedBodyViewer-SFML.dir/clean:
	cd /home/rstarritt/Documents/CSCI473/AstraSDK-v2.0.15-232757cc1d-20190327T080423Z-Linux/samples/sfml/ColorizedBodyViewer-SFML && $(CMAKE_COMMAND) -P CMakeFiles/ColorizedBodyViewer-SFML.dir/cmake_clean.cmake
.PHONY : sfml/ColorizedBodyViewer-SFML/CMakeFiles/ColorizedBodyViewer-SFML.dir/clean

sfml/ColorizedBodyViewer-SFML/CMakeFiles/ColorizedBodyViewer-SFML.dir/depend:
	cd /home/rstarritt/Documents/CSCI473/AstraSDK-v2.0.15-232757cc1d-20190327T080423Z-Linux/samples && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/rstarritt/Documents/CSCI473/AstraSDK-v2.0.15-232757cc1d-20190327T080423Z-Linux/samples /home/rstarritt/Documents/CSCI473/AstraSDK-v2.0.15-232757cc1d-20190327T080423Z-Linux/samples/sfml/ColorizedBodyViewer-SFML /home/rstarritt/Documents/CSCI473/AstraSDK-v2.0.15-232757cc1d-20190327T080423Z-Linux/samples /home/rstarritt/Documents/CSCI473/AstraSDK-v2.0.15-232757cc1d-20190327T080423Z-Linux/samples/sfml/ColorizedBodyViewer-SFML /home/rstarritt/Documents/CSCI473/AstraSDK-v2.0.15-232757cc1d-20190327T080423Z-Linux/samples/sfml/ColorizedBodyViewer-SFML/CMakeFiles/ColorizedBodyViewer-SFML.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : sfml/ColorizedBodyViewer-SFML/CMakeFiles/ColorizedBodyViewer-SFML.dir/depend

