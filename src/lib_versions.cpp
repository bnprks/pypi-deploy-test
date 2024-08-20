#include <Eigen/src/Core/util/Macros.h>
#include <H5public.h>


#include <string>


namespace example_package {
std::string hdf5_version() {
    unsigned int maj, min, rel;
    H5get_libversion(&maj, &min, &rel);
    return std::to_string(maj) + "." + std::to_string(min) + "." + std::to_string(rel);
}

std::string eigen_version() {
    return std::to_string(EIGEN_WORLD_VERSION) + "." + std::to_string(EIGEN_MAJOR_VERSION) + "." + std::to_string(EIGEN_MINOR_VERSION);
}

}