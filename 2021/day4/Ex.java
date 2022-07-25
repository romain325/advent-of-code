import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;
import java.util.concurrent.atomic.AtomicInteger;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class Ex {
    public static void main(String[] args) {
        File file = new File("./input2");
        List<boolean[][]> mask = new LinkedList<>();
        List<int[][]> grid = grids(file);
        for (int i = 0; i < grid.size(); i++) {
            boolean[][] arr = new boolean[5][5];
            for (boolean[] booleans : arr) {
              Arrays.fill(booleans, false);
            }
            mask.add(arr);
        }

        for(int entry : entries(file)) {
            for(int i = 0; i < grid.size(); i++) {
                boolean[][] val = mask.get(i);
                for (int i1 = 0; i1 < 5; i1++) {
                    for (int i2 = 0; i2 < 5; i2++) {
                        val[i1][i2] = val[i1][i2] || grid.get(i)[i1][i2] == entry;
                    }
                }
                System.out.println(Arrays.deepToString(mask.toArray()));
                System.out.println(Arrays.toString(mask.get(2)[0]));
                Arrays.asList(...mask.get(2)[0]).forEach(System.out::println);

                System.out.println(Arrays.asList(mask.get(2)[0]).contains(false));
                if(mask.stream().anyMatch(x -> Arrays.stream(x).anyMatch(y -> Arrays.asList(y).contains(false)))){
                  System.out.println(i);
                  System.out.println(Arrays.deepToString(val));
                  System.exit(0);
                }
            }
        }
        System.out.println(Arrays.deepToString(mask.toArray()));
    }

    private static List<Integer> entries(File f) {
        try(BufferedReader stream = new BufferedReader(new FileReader(f))){
            return Arrays.stream(stream.readLine().split(",")).map(Integer::parseInt).collect(
                Collectors.toList());
        } catch (IOException e) {
            e.printStackTrace();
        }
        return null;
    }

    private static List<int[][]> grids(File f) {
        List<int[][]> grid = new LinkedList<>();
        try(BufferedReader stream = new BufferedReader(new FileReader(f))){
            // dc
            stream.readLine();
            stream.readLine();

            AtomicInteger cnt = new AtomicInteger();
            Stream<String> lines = stream.lines();
      lines.forEach(
          line -> {
            if (line.isEmpty()) return;
            if (cnt.get() % 5 == 0) grid.add(new int[5][5]);
            grid.get(cnt.get()/5)[cnt.get() % 5] =
                Arrays.stream(line.trim().split("\\s+")).mapToInt(Integer::parseInt).toArray();
            cnt.getAndIncrement();
          });
        } catch (IOException e) {
            e.printStackTrace();
        }
        return grid;
    }
}
