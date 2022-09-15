cmake_minimum_required(VERSION 3.1)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

get_filename_component(ProjectId
    ${CMAKE_CURRENT_SOURCE_DIR} NAME)
string(REPLACE " " "_" ProjectId ${ProjectId})
project(${ProjectId})

add_executable(${PROJECT_NAME}.exe
    main.cxx)

#
# #
# ##
add_subdirectory(externals/std_math)
target_link_libraries(${PROJECT_NAME}.exe test)

#
# #
# ##

# SAMPLE FOR ADDING LIBRARY VIA SUBMODULE 1 of 2
#[[
find_package(OpenCV REQUIRED)

message(STATUS "OpenCV library status:")
message(STATUS "    config: ${OpenCV_DIR}")
message(STATUS "    version: ${OpenCV_VERSION}")
message(STATUS "    libraries: ${OpenCV_LIBS}")
message(STATUS "    include path: ${OpenCV_INCLUDE_DIRS}")

]]

#[[
    ADD LOGIC TO AUTOMATE FIND ANY PACKAGE WITH SUBMODULE(S)
]]

# SAMPLE FOR ADDING LIBRARY VIA GIT 2 of 2
#[[
target_link_libraries(${PROJECT_NAME}.exe PRIVATE ${OpenCV_LIBS})
]]

#
# #
# ##

#[[ <PACKAGE> EXAMPLE -> SubModule ]]

#[[

cmake_minimum_required(VERSION 3.23.2)

project(EXAMPLE)

add_executable(${PROJECT_NAME}.exe main.cxx)


add_subdirectory(external/<PACKAGE>)
add_subdirectory(/location/to/be/added)

target_include_directories(${PROJECT_NAME}.exe 
                PUBLIC external/<PACKAGE>/)

target_link_directories(${PROJECT_NAME}.exe
                        PRIVATE external/<PACKAGE>/src)

target_link_libraries(${PROJECT_NAME}.exe <PACKAGE>)

]]