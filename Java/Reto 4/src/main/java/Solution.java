//LA IMPORTACIÓN SIGUIENTE ES
//NECESARIA PARA MANIPULAR EL
//PARÁMETRO DE ENTRADA DE SU
//PROPUESTA DE SOLUCIÓN. NO LA
//DESCARTE
import java.util.ArrayList;
import java.util.Arrays;

public class Solution{
    public static Object [] reporte(ArrayList <Corredor> carrera){
        Object[] retorno = new Object[5];
        //ESCRIBA LA LÓGICA DE SU PROPUESTA
        //DE SOLUCIÓN. NO OLVIDE INDICAR EL
        //OBJETO QUE ESTA VA A RETORNAR
        double acumuladorTiempo = 0;
        double arregloHoras[]= new double[carrera.size()];
        for (int i = 0; i <carrera.size() ; i++) {
            acumuladorTiempo+= carrera.get(i).getTiempoMeta();
            arregloHoras[i]= carrera.get(i).getTiempoMeta();
        }
        Arrays.sort(arregloHoras);
        for (int j = 0; j <carrera.size() ; j++) {
            if(arregloHoras[0] == carrera.get(j).getTiempoMeta()){
                retorno[1]= carrera.get(j).getNombreCompleto();
                retorno[2]= carrera.get(j).getTiempoMeta();
            }
            if (arregloHoras[(carrera.size())-1] == carrera.get(j).getTiempoMeta()){
                retorno[3]= carrera.get(j).getNombreCompleto();
                retorno[4]= carrera.get(j).getTiempoMeta();
            }
        }
        retorno[0] = acumuladorTiempo/carrera.size();
        return retorno;
    }
}