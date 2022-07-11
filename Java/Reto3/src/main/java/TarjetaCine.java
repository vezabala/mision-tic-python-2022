public class TarjetaCine {
    //Atributos
    public String idTarjeta;
    public String nombreCompleto;
    public String email;
    public String telefono;
    public int edad;
    public double porcentajeDescuento;

    //Constructor
    public TarjetaCine(String idTarjeta, String nombreCompleto, String email, String telefono, int edad, double porcentajeDescuento) {
        this.idTarjeta = idTarjeta;
        this.nombreCompleto = nombreCompleto;
        this.email = email;
        this.telefono = telefono;
        this.edad = edad;
        this.porcentajeDescuento = porcentajeDescuento;
    }

    //Método
    public double pagar(String[] cuenta){
        int total= 0;
        double totalCuenta= 0;
        for (int i = 0; i <cuenta.length ; i++) {
            if(cuenta[i].equals("Boleta")){
                total += 6000;
            }else if(cuenta[i].equals("Combo 1 - Crispetas + Gaseosa")){
                total += 8000;
            }else if(cuenta[i].equals("Combo 2 - Perro + Gaseosa")){
                total += 12000;
            }
        }
        totalCuenta= total*(1-(porcentajeDescuento/100));
        return totalCuenta;
    }

    //Getters y Setters

    public String getIdTarjeta() {
        return idTarjeta;
    }

    public void setIdTarjeta(String idTarjeta) {
        this.idTarjeta = idTarjeta;
    }

    public String getNombreCompleto() {
        return nombreCompleto;
    }

    public void setNombreCompleto(String nombreCompleto) {
        this.nombreCompleto = nombreCompleto;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public String getTelefono() {
        return telefono;
    }

    public void setTelefono(String telefono) {
        this.telefono = telefono;
    }

    public int getEdad() {
        return edad;
    }

    public void setEdad(int edad) {
        this.edad = edad;
    }

    public double getPorcentajeDescuento() {
        return porcentajeDescuento;
    }

    public void setPorcentajeDescuento(double porcentajeDescuento) {
        this.porcentajeDescuento = porcentajeDescuento;
    }
}
