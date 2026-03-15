cmake_minimum_required(VERSION 3.16)

# Project name and C++ standard
project(TesseractAI VERSION 1.0 LANGUAGES CXX)
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

# Include directories (so compiler can find your .hpp files)
include_directories(${PROJECT_SOURCE_DIR}/include)

# Collect source files
set(SOURCES
    src/main.cpp
    src/board.cpp
    src/agent.cpp
    src/game.cpp
)

# Create the executable
add_executable(tesseract ${SOURCES})

# Optional: specify output directory
set_target_properties(tesseract PROPERTIES
    RUNTIME_OUTPUT_DIRECTORY ${PROJECT_BINARY_DIR}/bin
)

# Optional: add warning flags
if(MSVC)
    target_compile_options(tesseract PRIVATE /W4 /permissive-)
else()
    target_compile_options(tesseract PRIVATE -Wall -Wextra -Wpedantic -O3)
endif()