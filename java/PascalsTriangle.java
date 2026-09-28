void main() {
    int layerNum = Integer.parseInt(IO.readln("Enter the number of layers:\n"));

    for (int i = layerNum; i >= 0; i--) {
        for (int j = 0; j <= i; j++) {
            IO.print(choose(i, j));
            if (j != i) {
                IO.print(" ");
            }
        }
        IO.println();
    }
}

int factorial(int num) {
    int result = 1;
    for (int i = 1; i <= num; i++) {
        result *= i;
    }
    return result;
}

int choose(int n, int r) {
    return factorial(n) / (factorial(n - r) * factorial(r));
}