// Copyright 2023 BPCells contributors
// 
// Licensed under the Apache License, Version 2.0 <LICENSE-APACHE or
// https://www.apache.org/licenses/LICENSE-2.0> or the MIT license
// <LICENSE-MIT or https://opensource.org/licenses/MIT>, at your
// option. This file may not be copied, modified, or distributed
// except according to those terms.

#include <pybind11/pybind11.h>
#include <stdexcept>
#include <string>

#include "add.h"
#include "hwy_target.h"
#include "lib_versions.h"

PYBIND11_MODULE(cpp, m) {

    m.def("add_two", &example_package::py::add_two);
    m.def("hwy_target", &example_package::current_target);
    m.def("hdf5_version", &example_package::hdf5_version);
    m.def("eigen_version", &example_package::eigen_version);
    m.def("zlib_version", &example_package::example_zlib_version);

#ifdef VERSION_INFO
    m.attr("__version__") = MACRO_STRINGIFY(VERSION_INFO);
#else
    m.attr("__version__") = "dev";
#endif

}
