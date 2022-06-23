import java.util.Arrays;

public class Reto1 {
    public static void main(String[]args){
        int [] participantes = {19, 22, 21, 25, 32, 38, 16, 31, 30, 26, 19, 17, 23 };
        reporte(participantes);
    }
    public static int [] reporte(int [] participantes){
        //EN ESTE ESPACIO PONER SU LÓGICA
        int[] resultados = new  int[3];
        resultados[0] = participantes.length;
        resultados[1] = participantes[0];
        resultados[2] = participantes[0];
        for (int i = 0; i < participantes.length; i++) {
            if (participantes[i]< resultados[1]) {
                resultados[1] = participantes[i];
            }else {
                if(participantes[i]> resultados[2]){
                    resultados[2]=participantes[i];
                }
            }
        }
        System.out.println(Arrays.toString(resultados));
        return resultados;
    }
}
