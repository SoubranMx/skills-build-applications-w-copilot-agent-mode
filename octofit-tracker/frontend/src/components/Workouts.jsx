import React, { useEffect, useState } from 'react';

const Workouts = () => {
  const [workouts, setWorkouts] = useState([]);
  const endpoint = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/workouts/`;

  useEffect(() => {
    console.log('Fetching from:', endpoint);
    fetch(endpoint)
      .then(res => res.json())
      .then(data => {
        const results = data.results || data;
        setWorkouts(results);
        console.log('Fetched workouts:', results);
      })
      .catch(err => console.error('Error fetching workouts:', err));
  }, [endpoint]);

  return (
    <div className="row justify-content-center">
      <div className="col-md-10">
        <div className="card shadow mb-4">
          <div className="card-header bg-success text-white">
            <h2 className="h4 mb-0">Workouts</h2>
          </div>
          <div className="card-body">
            <div className="table-responsive">
              <table className="table table-striped table-hover align-middle">
                <thead className="table-light">
                  <tr>
                    <th>#</th>
                    <th>Name</th>
                    <th>Type</th>
                    <th>Duration</th>
                    <th>Calories</th>
                  </tr>
                </thead>
                <tbody>
                  {workouts.map((workout, idx) => (
                    <tr key={workout.id || idx}>
                      <td>{idx + 1}</td>
                      <td>{workout.name || '-'}</td>
                      <td>{workout.type || '-'}</td>
                      <td>{workout.duration || '-'}</td>
                      <td>{workout.calories || '-'}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
              {workouts.length === 0 && <div className="text-muted">No data available.</div>}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Workouts;
