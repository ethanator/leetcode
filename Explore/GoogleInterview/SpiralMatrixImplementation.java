import java.util.ArrayList;
import java.util.List;

class SpiralMatrix {
  public static List<Integer> spiralOrder(int[][] matrix) {
    List<Integer> arr = new ArrayList<>();
    if (matrix.length == 0 || matrix[0].length == 0) {
      return arr;
    }
    
    int[][] DIRECTIONS = {{0,1},{1,0},{0,-1},{-1,0}};
    int rowIter = matrix[0].length,
        colIter = matrix.length - 1,
        dirIter = 0,
        x = 0,
        y = -1;
    while (rowIter >= 0 && colIter >= 0) {
      boolean dirFlag = dirIter % 2 == 0;
      int steps = dirFlag ? rowIter : colIter;
      for (int i = 0; i < steps; i++) {
        x += DIRECTIONS[dirIter][0];
        y += DIRECTIONS[dirIter][1];
        arr.add(matrix[x][y]);
      }
      if (dirFlag) {
        rowIter--;
      } else {
        colIter--;
      }
      dirIter = (dirIter + 1) % 4;
    }

    return arr;
  }
}

public class SpiralMatrixImplementation {
  public static void main(String[] args) {
    int[][] matrix = {
      { 1,  2,  3,  4 },
      { 5,  6,  7,  8 },
      { 9, 10, 11, 12 }
    };
    System.out.println(SpiralMatrix.spiralOrder(matrix));
  }
}