from conans import ConanFile, tools, os

class BoostVmdConan(ConanFile):
    name = "Boost.Vmd"
    version = "1.64.0"
    generators = "txt"
    url = "https://github.com/boostorg/vmd"
    description = "Please visit http://www.boost.org/doc/libs/1_64_0/libs/libraries.htm"
    license = "www.boost.org/users/license.html"
    lib_short_name = "vmd"
    requires = "Boost.Preprocessor/1.64.0@bincrafters/testing"
    
    def source(self):
        self.run("git clone --depth=50 --branch=boost-{0} {1}.git"
                 .format(self.version, self.url))

    def package(self):
        include_dir = os.path.join(self.build_folder, self.lib_short_name, "include")
        self.copy(pattern="*", dst="include", src=include_dir)

    def package_id(self):
        self.info.header_only()