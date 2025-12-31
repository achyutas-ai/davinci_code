#include <iostream>
#include <fstream>
#include <string>

int main(int argc, char* argv[]) {
    if (argc < 2) {
        std::cerr << "Prompt required\n";
        return 1;
    }

    std::string prompt = argv[1];

    // Simulate inference
    std::ofstream out("output.txt");
    out << "Generated image for prompt: " << prompt << "\n";
    out.close();

    // Machine-readable output for FastAPI
    std::cout << "{ \"status\": \"success\", \"output\": \"output.txt\" }";

    return 0;
}
