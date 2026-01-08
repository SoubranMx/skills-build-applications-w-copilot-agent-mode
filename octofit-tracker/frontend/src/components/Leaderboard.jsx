import React, { useEffect, useState } from 'react';

const Leaderboard = () => {
  const [leaders, setLeaders] = useState([]);
  const endpoint = `https://${import.meta.env.VITE_CODESPACE_NAME}-8000.app.github.dev/api/leaderboard/`;

  useEffect(() => {
    console.log('Fetching from:', endpoint);
    fetch(endpoint)
      .then(res => res.json())
      .then(data => {
        const results = data.results || data;
        setLeaders(results);
        console.log('Fetched leaderboard:', results);
      })
      .catch(err => console.error('Error fetching leaderboard:', err));
  }, [endpoint]);

  return (
    <div className="row justify-content-center">
      <div className="col-md-8">
        <div className="card shadow mb-4">
          <div className="card-header bg-primary text-white">
            <h2 className="h4 mb-0">Leaderboard</h2>
          </div>
          <div className="card-body">
            <div className="table-responsive">
              <table className="table table-striped table-hover align-middle">
                <thead className="table-light">
                  <tr>
                    <th>#</th>
                    <th>Name</th>
                    <th>Score</th>
                  </tr>
                </thead>
                <tbody>
                  {leaders.map((leader, idx) => (
                    <tr key={leader.id || idx}>
                      <td>{idx + 1}</td>
                      <td>{leader.name || leader.username || leader.user || '-'}</td>
                      <td>{leader.score || leader.points || '-'}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
              {leaders.length === 0 && <div className="text-muted">No data available.</div>}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Leaderboard;
