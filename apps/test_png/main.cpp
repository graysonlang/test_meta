#include <libpng/png.h>

#include <algorithm> // min, max
#include <chrono>
#include <cstddef>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <vector>

double elapsed() {
    static std::chrono::time_point<std::chrono::system_clock> s_start = std::chrono::system_clock::now();
    std::chrono::duration<double> elapsed_seconds = std::chrono::system_clock::now() - s_start;
    return elapsed_seconds.count();
}

void test_libpng(const char *in_filename, const char *out_filename) {
    png_image image;
    memset(&image, 0, (sizeof image));
    image.version = PNG_IMAGE_VERSION;
    image.format = PNG_FORMAT_RGBA;

    elapsed();
    int result_code = png_image_begin_read_from_file(&image, in_filename);
    if (result_code == 0) {
    } else {
        png_bytep buffer;
        buffer = (png_byte*) malloc(PNG_IMAGE_SIZE(image));
        if (buffer != NULL && png_image_finish_read(&image, NULL/*background*/, buffer, 0/*row_stride*/, NULL/*colormap*/) != 0) {
        }
    }
    printf("%.2f seconds\n", elapsed());
}

int main(int argc, const char *argv[]) {
    if (argc < 2) {
        printf("Expecting input PNG filename.\n");
        exit(1);
    }

    const char *in_filename = argv[1];
    const char *out_filename = argc > 2 ? argv[2] : "output.png";

    test_libpng(in_filename, out_filename);

    exit(0);
}
