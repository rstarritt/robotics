#SFML path varies depending upon if we're building the full SDK or just sample directory
if (ASTRA_SDK_BUILD)
  if (ASTRA_OSX)
    set(SFML_PATH "${ASTRA_SDK_SOURCE_DIR}/samples-aux/thirdparty-bin/osx/sfml-2.3.2-min/")
  elseif(ASTRA_WINDOWS)
      if (ASTRA_64)
          set(BIT_DIR "64")
      else()
          set(BIT_DIR "32")
      endif()
      set(SFML_PATH "${ASTRA_SDK_SOURCE_DIR}/samples-aux/thirdparty-bin/${VS_DIR}/thirdparty/SFML-min-${BIT_DIR}/")
  else()
      set(SFML_PATH "SFML_ROOT-UNDEFINED")
  endif()
else()
  if (ASTRA_OSX)
      set(SFML_PATH "${CMAKE_SOURCE_DIR}/thirdparty/sfml-2.3.2-min/")
  elseif(ASTRA_WINDOWS)
      if (ASTRA_64)
          set(BIT_DIR "64")
      else()
          set(BIT_DIR "32")
      endif()
      set(SFML_PATH "${CMAKE_SOURCE_DIR}/${VS_DIR}/thirdparty/sfml-min-${BIT_DIR}/")
  endif()
endif()



if (DEFINED SFML_PATH)
  if (NOT EXISTS "${SFML_PATH}")
    message(STATUS "SFML is not in expected path: ${SFML_PATH}")
  else()
    message(STATUS "Using SFML path: ${SFML_PATH}")
    set(CMAKE_PREFIX_PATH ${CMAKE_PREFIX_PATH} "${SFML_PATH}")
  endif()
endif()

add_subdirectory(SimpleDepthViewer-SFML)
add_subdirectory(SimpleStreamViewer-SFML)
add_subdirectory(SimpleColorViewer-SFML)
add_subdirectory(MultiSensorViewer-SFML)
add_subdirectory(SimpleBodyViewer-SFML)
add_subdirectory(MaskedColorViewer-SFML)
add_subdirectory(ColorizedBodyViewer-SFML)

if (OBT_BUILD_STANDALONE AND ASTRA_PACKAGER_REAL_BODY_TRACKING)
  add_subdirectory(StandaloneBodyViewer-SFML)
endif()

if (ASTRA_HAND)
    add_subdirectory(SimpleHandViewer-SFML)
endif()

if (ASTRA_WINDOWS)
  set(FONT_TARGET_DIR "${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/$<CONFIG>")
else()
  set(FONT_TARGET_DIR "${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/")
endif()

if (ASTRA_SDK_BUILD)
  install_file(${PROJECT_SOURCE_DIR}/vendor/Inconsolata.otf bin)
endif()

if (ASTRA_OSX)
  add_custom_target(copy-sample-files ALL
    COMMAND ${CMAKE_COMMAND} -E copy
    "${PROJECT_SOURCE_DIR}/vendor/Inconsolata.otf"
    ${FONT_TARGET_DIR})

  set_target_properties(copy-sample-files PROPERTIES FOLDER CMakeCopyTargets)

  add_custom_command(TARGET copy-sample-files POST_BUILD
    COMMAND cp
    -R
    ${SFML_PATH}/lib/
    ${CMAKE_ARCHIVE_OUTPUT_DIRECTORY}/)

  if (ASTRA_SDK_BUILD)
    install_dir(${SFML_PATH}/lib/ lib)
    install_dir(${SFML_PATH} samples/thirdparty/sfml-2.3.2-min)
  endif()
endif()
