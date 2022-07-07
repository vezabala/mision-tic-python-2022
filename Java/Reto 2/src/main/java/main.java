import java.util.Arrays;

public class main {
    public static void main(String[] args) {
        String [] cancionesEscogidas = new String [] { "Mil horas",
                "Por ese hombre", "A esa",
                "Algo de mi",
                "Si me dejas ahora", "¿Quieres ser mi amante?", "Quel sorriso in volto", "Per una notte insieme", "Como un pintor",
                "Sencillamente", "Un segundo","Enciéndeme",
                "Cuando me enamoro", "Tu eres mi tesoro", "Piccola anima",
                "Solo a ti pertenezco", "Todos por todos"
        };

        ReproductorMusica ventana1 =new ReproductorMusica(cancionesEscogidas);
        //Screenshot 2
        ventana1.devolverCancion();
        ventana1.devolverCancion();
        ventana1.devolverCancion();
        ventana1.devolverCancion();
        System.out.println(Arrays.toString(ventana1.getCancionesFavoritas()));
        System.out.println(ventana1.isPausado());
        System.out.println(ventana1.getCancionReproduciendo());
        //Screenshot 3
        ventana1.agregarCancionesFavoritas();
        ventana1.proximaCancion();
        ventana1.agregarCancionesFavoritas();
        ventana1.devolverCancion();
        ventana1.agregarCancionesFavoritas();

        //Screenshot 4
        ventana1.cambiarEstadoReproduccion();
        ventana1.cambiarEstadoReproduccion();
        ventana1.cambiarEstadoReproduccion();
        ventana1.cambiarEstadoReproduccion();
        ventana1.cambiarEstadoReproduccion();

    }
}
