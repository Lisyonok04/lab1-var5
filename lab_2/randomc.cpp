#include <iostream>
#include <random>
using namespace std;
/*
 * The function for generating random numbers in a given range
 * @param a, b The ranges for generating a random number
 * @return A random number from the random function
 */
int random(int a, int b) {
    random_device random_device;
    mt19937 generator(random_device());
    uniform_int_distribution<> segment(a, b);
    int x = segment(generator);
    return x;
}

/*
 * The function for generating a random sequence of
 * bits of a given length and displaying it on the screen
 * @param n The number of bits in the sequence 
 */
void RandomGenerator(int n) {
    for(int i = 0; i < n; i++) 
        cout << random(0, 1);
}

int main() {
    const int BTS = 128;
    RandomGenerator(BTS);
    return 0; 
}