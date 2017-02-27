#include <stdio.h>

int fact(int n) {
    if (n == 0)
        return 1;
    return n * fact(n - 1);
}

int main(int argc, char* argv[]) {
    int a;
    int b;
    printf("hello world! %d", a);
    fputc(a, b);
    return 0;
}
