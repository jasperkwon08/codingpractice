void main() {
    int layerNum = Integer.parseInt(IO.readln("Enter the number of layers:\n"));
    int[][][] pyramid = new int[layerNum][layerNum][layerNum];

    pyramid[0][0][0] = 1;

    for (int i = 1; i < layerNum; i++) {
        for (int j = 0; j <= i; j++) {
            for (int k = 0; k <= j; k++) {
                pyramid[i][j][k] = pyramid[i - 1][j][k];

                if (j > 0) {
                    pyramid[i][j][k] += pyramid[i - 1][j - 1][k];
                }
                if (j > 0 && k > 0) {
                    pyramid[i][j][k] += pyramid[i - 1][j - 1][k - 1];
                }
            }
        }
    }

    for (int j = 0; j < layerNum; j++) {
        for (int k = 0; k <= j; k++) {
            IO.print(pyramid[layerNum - 1][j][k]);

            if (k != j) {
                IO.print(" ");
            }
        }
        IO.println();
    }
}