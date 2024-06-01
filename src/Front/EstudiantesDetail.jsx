import React from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import Tabla from './Components/Table';

const tablaMaterias = [
  { header: 'Materia', accessor: 'nombre' },
  { header: 'Nota', accessor: 'nota' },
];

const txt = "text-gray-200";
export default function EstudiantesDetail({ estudiantes }) {
  const { legajo } = useParams();
  const navigate = useNavigate();
  const estudiante = estudiantes.find(e => e.legajo === legajo);

  if (!estudiante) {
    return <div>Estudiante no encontrado</div>;
  }

  return (
    <div className="flex justify-center min-h-screen p-4 bg-zinc-900 rounded-xl">
      <div className="bg-zinc-800 shadow-lg rounded-lg overflow-hidden w-11/12 max-w-2xl p-6">
        <h2 className="text-3xl font-bold mb-6 text-center">Detalles del Estudiante</h2>
        <div className="mb-4 text-left">
          <p className={`${txt} text-lg font-semibold `}>Apellido/s: {estudiante.nombre}</p>
          <p className={`${txt} text-lg font-semibold`}>Nombre/s: {estudiante.apellido}</p>
          <p className={txt}>Legajo: {estudiante.legajo}</p>
          <p className={txt}>Edad: {estudiante.edad}</p>
          <p className={txt}>Carrera: {estudiante.carrera}</p>
          <p className={txt}>Email: {estudiante.email}</p>
          <p className={txt}>Teléfono: {estudiante.telefono}</p>
          <p className={txt}>Dirección: {estudiante.direccion}</p>
        </div>
        <div className="mb-4">
          <h3 className="text-2xl font-semibold">Materias que cursa</h3>
          <Tabla columnas={tablaMaterias} datos={estudiante.materias} />
        </div>
        <button
          className="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-700"
          onClick={() => navigate(-1)}
        > Volver </button>
      </div>
    </div>
  );
}