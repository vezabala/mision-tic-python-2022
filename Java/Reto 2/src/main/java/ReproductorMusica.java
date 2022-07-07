public class ReproductorMusica {

    //ATRIBUTOS
    private String[] canciones;
    private int[] cancionesFavoritas;
    private boolean pausado;
    private  int cancionReproduciendo;

    //MÉTODOS


    public ReproductorMusica(String[] canciones) {
        this.canciones = canciones;
        this.cancionesFavoritas = new int[canciones.length];
        for (int i = 0; i <cancionesFavoritas.length ; i++) {
            cancionesFavoritas[i] = -1;
        }
        this.pausado = true;
        this.cancionReproduciendo = 0;
    }

    public void proximaCancion(){
        //COMPLETE AQUÍ LA LÓGICA DE ESTE MÉTODO SEGÚN EL ENUNCIADO
        this.cancionReproduciendo = (cancionReproduciendo + 1) % canciones.length;
    }

    public void devolverCancion(){
        //COMPLETE AQUÍ LA LÓGICA DE ESTE MÉTODO SEGÚN EL ENUNCIADO
        this.cancionReproduciendo = (cancionReproduciendo +canciones.length -1)%canciones.length;
    }

    public void cambiarEstadoReproduccion(){
        //COMPLETE AQUÍ LA LÓGICA DE ESTE MÉTODO SEGÚN EL ENUNCIADO
        if (this.pausado = true){
            pausado = false;
        } else {
            pausado = true;
        }
    }


    //NO SE DEBE PREOCUPAR POR DESARROLLAR ESTE MÉTODO. ¡NO ELIMINARLO NI MODIFICARLO!

    public void agregarCancionesFavoritas(){
        for(int i = 0; i < cancionesFavoritas.length; i++)
            /*En caso de que encuentre que cancionReproduciendo está en el banco de cancionesFavoritas
            no seguimos buscando espacio libre para agregarla, y salimos del método*/
            if(cancionesFavoritas[i] == cancionReproduciendo)
                return;
                //Pero si no la encontró, y además encuentra un espacio donde añadirlo, lo hace
            else if(cancionesFavoritas[i] == -1){
                cancionesFavoritas[i] = cancionReproduciendo;
                return;
            }
    }

    public String[] getCanciones() {
        return canciones;
    }

    public void setCanciones(String[] canciones) {
        this.canciones = canciones;
    }

    public int[] getCancionesFavoritas() {
        return cancionesFavoritas;
    }

    public void setCancionesFavoritas(int[] cancionesFavoritas) {
        this.cancionesFavoritas = cancionesFavoritas;
    }

    public boolean isPausado() {
        return pausado;
    }

    public void setPausado(boolean pausado) {
        this.pausado = pausado;
    }

    public int getCancionReproduciendo() {
        return cancionReproduciendo;
    }

    public void setCancionReproduciendo(int cancionReproduciendo) {
        this.cancionReproduciendo = cancionReproduciendo;
    }
}
