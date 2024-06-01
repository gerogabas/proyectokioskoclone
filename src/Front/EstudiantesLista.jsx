import React, { useState } from "react";
import { Link } from "react-router-dom";
import Tabla from "./Components/Table";
import ModalConfirmacion from "./Components/ModalConfirmacion";
import RadioButton from "./Components/FiltroConSwitch";

const btn1 = "bg-transparent hover:bg-pink-900 text-pink-300 hover:text-white py-2 px-4 rounded font-bold border border-pink-600 hover:border-transparent ";
const btn2 = "bg-transparent hover:bg-red-700  text-red-500  hover:text-white py-2 px-4 rounded font-bold border border-red-900 hover:border-transparent hover:";
const columnas = [
  { header: "Legajo", accessor: "legajo" },
  { header: "Apellido", accessor: "apellido" },
  { header: "Nombre", accessor: "nombre" },
  { header: "Carrera", accessor: "carrera" },
  { header: "Email", accessor: "email" },
  { header: "Ver/Editar", accessor: "ver" },
  { header: "Eliminar", accessor: "eliminar" },
];

export default function EstudiantesLista({ estudiantes, onEliminar }) {
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [selectedLegajo, setSelectedLegajo] = useState(null);

  //data para testeo

  if (!estudiantes) {
    estudiantes = [
      {
        nombre: "Nombres",
        apellido: "Apellidos",
        legajo: "12345",
        edad: 20,
        carrera: "Carreras",
        email: "juan.perez@example.com",
        telefono: "123-456-7890",
        direccion: "Calle Falsa 123, Ciudad, País",
        materias: [
          { nombre: "Álgebra", nota: "A" },
          { nombre: "Cálculo", nota: "B" },
          { nombre: "Estadística", nota: "A" },
        ],
      }
    ];
    //return <div>Error al acceder a los estudiantes...</div>;
  }
  else if (estudiantes.length === 0){
    return <div>No hay estudiantes en la bdd...</div>;
  }

  const handleEliminarClick = (legajo) => {
    setSelectedLegajo(legajo);
    setIsModalOpen(true);
  };

  const handleConfirm = async () => {
    try {
      const response = await fetch(`/api/estudiantes/${selectedLegajo}`, {
        method: 'DELETE',
      });
      if (!response.ok) {
        throw new Error('Error al eliminar el estudiante');
      }
      onEliminar(selectedLegajo);  // Actualizar la lista en el componente App
    } catch (error) {
      console.error("Error al eliminar el estudiante:", error);
    }
  };

  const datos = estudiantes.map((estudiante) => ({
    ...estudiante,
    ver: (
      <Link
        to={`/estudiantes/${estudiante.legajo}`}
        className={btn1}
      > Ver </Link>
    ),
    eliminar: (
      <button
        onClick={() => handleEliminarClick(estudiante.legajo)}
        className={`${btn2} hover:shadow-lg hover:shadow-red-600`}
      > Eliminar </button>
    ),
  }));

  return (
    <div className="min-h-screen bg-zinc-900 p-4 rounded-xl">
      <RadioButton />
      <Tabla title={"Estudiantes"} columnas={columnas} datos={datos} />
      <ModalConfirmacion
        isOpen={isModalOpen}
        onClose={() => setIsModalOpen(false)}
        onConfirm={handleConfirm}
        identifier={selectedLegajo}
        entityName="estudiante"
      />
    </div>
  );
}
