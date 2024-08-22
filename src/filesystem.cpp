#include "filesystem.h"
#include <string>

#include "filesystem_compat.h"

namespace example_package {
    bool path_exists(const std::string &path) {
        return std_fs::exists(std_fs::path(path));        
    }
}