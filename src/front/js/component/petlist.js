import React from 'react';
import { Link } from 'react-router-dom';

const PetList = ({ pets, handleOpenModal, handleAddPet }) => {
  const addPet = (newPet) => {
    handleAddPet(newPet);
    handleOpenModal();
  }

  return (
    <React.Fragment>
      {pets.length > 0 ? (
        <div className="section-your-pets">
          <h3 className='mb-5'>Tus Mascotas:</h3>
          <div className="card-container card-mis-mascotas">
            {pets && pets.map((pet, index) => (
              <div key={index} className="card card-mis-mascotas">
                <Link to={`/detalle-mascota/${index}`} className="detalle-link">
                  <img src={pet.foto} alt={pet.nombre} className="card-img-top" />
                  <div className="card-body">
                    <h5 className="card-title">{pet.nombre}</h5>
                    <i className="fas fa-plus-circle"></i>
                  </div>
                </Link>
              </div>
            ))}
          </div>
          <button className="btn btn-primary" onClick={handleOpenModal}>
            Agregar Otra Mascota
          </button>
        </div>
      ) : (
        <div className="section-add-pet">
          <h3 className='m-5'>¡No tienes mascotas registradas, agrega una ahora! <i className="fas fa-paw"></i></h3>
          <button className="btn btn-primary" onClick={handleOpenModal}>
            Agregar Mascota
          </button>
        </div>
      )}
    </React.Fragment >
  )
}

export default PetList;