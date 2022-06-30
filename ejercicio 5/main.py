from repositorioPacientes import RepositorioPacientes
from vistaPacientes import PacientesView
from controladorPacientes import ControladorPacientes
from objectEncoder import ObjectEncoder

def main():
    conn = ObjectEncoder('pacientes.json')
    repo = RepositorioPacientes(conn)
    vista = PacientesView()
    ctrl = ControladorPacientes(repo, vista)
    vista.setControlador(ctrl)
    ctrl.start()
    ctrl.salirGrabarDatos()

if __name__ == "__main__":
    main()