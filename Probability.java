package ru.itis;

import Jama.Matrix;

import java.io.*;
import java.util.ArrayList;
import java.util.Arrays;

/**
 * Created by IntelliJ IDEA
 * Date: 11.05.2022
 * Time: 2:59 PM
 *
 * @author lordvidex
 * Name: Овамойо Олувадамилола Эванс
 * <p>
 * Desc:
 */
public class Probability {
    static int totalSize;
    static double rsquared;
    static int v = 11;
    static double[] q = new double[]{96 + v, 95 + v, 92 + v, 94 + v, 92 + v, 95 + v, 93 + v, 98 + v, 98 + v, 97 + v, 99 + v, 96 + v, 94 + v, 98 + v, 96 + v, 98 + v};
    public static void main(String[] args) {
//        try {

//            Matrix xMatrix = readFileAndGetX();
//            Matrix yMatrix = readFileAndGetY();
        double[] p = new double[] {2,2.3,4.1,3.1,4,2.7,3.6,1, 1.2,1.3,0.7,2,3,0.8,2.1,1};
        double[] y = new double[]{-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1, -1, -1, -1, -1, -1};

        Matrix xMatrix = readXMatrix(p,y);
        Matrix yMatrix = readYMatrix(q);
        Matrix result = (((xMatrix.transpose().times(xMatrix)).inverse()).times(xMatrix.transpose())).times(yMatrix);
        System.out.println(Arrays.deepToString(result.getArray()));
        solveRsquared(q, result.get(0,0), result.get(1,0), result.get(2,0), p, y);
        last();
//        } catch (IOException e) {
//            System.out.println("An error occured");
//        }
    }

    static void solveRsquared(double[] q, double b0, double b1, double b2, double[] p, double[] y) {
        double numerator = 0;
        double denominator = 0;
        for (int i = 0; i < q.length; i++) {
            numerator += Math.pow(q[i] - (b0+b1*p[i]+b2*y[i]), 2);
        }
        for (int i = 0; i < q.length; i++) {
            denominator += Math.pow(q[i] - mean(q), 2);
        }
        rsquared = 1 - numerator/denominator;
        System.out.println(rsquared);
    }

    static void last() {
        int k = 3;
        int n = q.length;
        double answer = 1 - (1 - rsquared) * ((float)(n-1)/(n-k));
        System.out.println(answer);
    }

    static double mean(double[] val) {
        double sum = 0;
        for (int i = 0; i < val.length; i++) {
            sum+=val[i];
        }
        return sum / val.length;
    }
    static Matrix readXMatrix(double[] p, double[] y) {
        if (p.length != y.length) {
            System.err.println("P and Y must have the same length");
            System.exit(-1);
        }
        double[][] arrs = new double[p.length][];
        for (int i = 0; i < p.length; i++) {
            double[] arr = new double[]{1, p[i], y[i]};
            arrs[i] = arr;
        }
        return new Matrix(arrs);
    }

    static Matrix readYMatrix(double[] q) {
        double[][] arrs = new double[q.length][];
        for (int i = 0; i < q.length; i++) {
            arrs[i] = new double[]{q[i]};
        }
        return new Matrix(arrs);
    }

    static Matrix readFileAndGetX() throws IOException {
        ArrayList<double[]> rows = new ArrayList<>();
        File file = new File("/Users/lordvidex/IdeaProjects/probability/src/main/java/ru/itis/EURUSD.csv");
        BufferedReader br = new BufferedReader(new FileReader(file));
        br.readLine();
        String line;
        while((line = br.readLine()) != null) {
            double[] d = new double[3];
            String[] splitted = line.split(",");
            d[0] = Double.parseDouble(splitted[4]);
            d[1] = Double.parseDouble(splitted[5]);
            d[2] = Double.parseDouble(splitted[6]);
            rows.add(d);
        }
        double[][] result = new double[rows.size()][];
        totalSize = rows.size();
        for(int i = 0; i < rows.size(); i++) {
            result[i] = rows.get(i);
        }
        return new Matrix(result);
    }

    static Matrix readFileAndGetY() throws IOException {
        double[][] y = new double[totalSize][];
        File file = new File("/Users/lordvidex/IdeaProjects/probability/src/main/java/ru/itis/EURUSD.csv");
        BufferedReader br = new BufferedReader(new FileReader(file));
        br.readLine();
        String line;
        int i = 0;
        while((line = br.readLine()) != null) {
            String[] splitted = line.split(",");
            y[i++] = new double[] {Double.parseDouble(splitted[7])};
        }
        return new Matrix(y);
    }


}
