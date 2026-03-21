cmake_minimum_required(VERSION 3.16)

project(TesseractAI VERSION 1.0 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

# Collect all .cpp files automatically
file(GLOB_RECURSE SOURCES CONFIGURE_DEPENDS
    ${PROJECT_SOURCE_DIR}/src/*.cpp
)

# Create executable
add_executable(tesseract ${SOURCES})

# Include directories
target_include_directories(tesseract PRIVATE
    ${PROJECT_SOURCE_DIR}/include
)

# Output directory
set_target_properties(tesseract PROPERTIES
    RUNTIME_OUTPUT_DIRECTORY ${PROJECT_BINARY_DIR}/bin
)

# Warnings
if(MSVC)
    target_compile_options(tesseract PRIVATE /W4 /permissive-)
else()
    target_compile_options(tesseract PRIVATE -Wall -Wextra -Wpedantic -O3)
endif()