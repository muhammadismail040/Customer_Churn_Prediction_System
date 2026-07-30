import { useEffect, useState } from "react";
import Modal from "react-bootstrap/Modal";
import Button from "react-bootstrap/Button";
import { saveAs } from "file-saver";

import DashboardCards from "./DashboardCards";
import PredictionCharts from "./PredictionCharts";

import {
  getPredictionHistory,
  getPredictionCount,
  getLatestPrediction,
  deletePrediction,
} from "../services/predictionService";

function PredictionHistory({ refresh }) {
  const [history, setHistory] = useState([]);
  const [count, setCount] = useState(0);
  const [latest, setLatest] = useState(null);

  const [selectedPrediction, setSelectedPrediction] = useState(null);
  const [showModal, setShowModal] = useState(false);
  const [searchTerm, setSearchTerm] = useState("");
  const [currentPage, setCurrentPage] = useState(1);
  const recordsPerPage = 5;

  const highRisk = history.filter((item) => item.prediction === "Yes").length;
  const lowRisk = history.filter((item) => item.prediction === "No").length;

  const averageProbability =
    history.length > 0
      ? (
          (history.reduce(
            (sum, item) => sum + item.probability,
            0
          ) /
            history.length) *
          100
        ).toFixed(2)
      : 0;

  // ==========================================
  // Load Data
  // ==========================================

  const loadData = async () => {
    try {
      const historyResponse = await getPredictionHistory();
      const countResponse = await getPredictionCount();
      const latestResponse = await getLatestPrediction();

      setHistory(historyResponse.data);
      setCount(countResponse.data.total_predictions);
      setLatest(latestResponse.data);
    } catch (error) {
      console.log(error);
    }
  };

  // ==========================================
  // Delete Prediction
  // ==========================================

  const handleDelete = async (id) => {
    const confirmDelete = window.confirm(
      "Are you sure you want to delete this prediction?"
    );

    if (!confirmDelete) {
      return;
    }

    try {
      await deletePrediction(id);
      loadData();
    } catch (error) {
      console.log(error);
      alert("Unable to delete prediction.");
    }
  };

  // ==========================================
  // View Prediction
  // ==========================================

  const handleView = (prediction) => {
    setSelectedPrediction(prediction);
    setShowModal(true);
  };

  const closeModal = () => {
    setShowModal(false);
    setSelectedPrediction(null);
  };

  // ==========================================
  // Page Load
  // ==========================================

  useEffect(() => {
    loadData();
  }, [refresh]);

  // ==========================================
  // Export CSV
  // ==========================================

  const exportCSV = () => {
    const headers = ["ID", "Prediction", "Probability", "Cluster", "Date"];

    const rows = history.map((item) => [
      item.id,
      item.prediction,
      (item.probability * 100).toFixed(2) + "%",
      item.cluster,
      new Date(item.created_at).toLocaleString(),
    ]);

    const csvContent = [headers, ...rows]
      .map((e) => e.join(","))
      .join("\n");

    const blob = new Blob([csvContent], {
      type: "text/csv;charset=utf-8;",
    });

    saveAs(blob, "prediction_history.csv");
  };

  // ==========================================
  // Filter History
  // ==========================================

  const filteredHistory = history.filter((item) => {
    return (
      item.id.toString().includes(searchTerm) ||
      item.prediction.toLowerCase().includes(searchTerm.toLowerCase()) ||
      item.cluster.toString().includes(searchTerm)
    );
  });

  // ==========================================
  // Pagination Logic
  // ==========================================

  const indexOfLastRecord = currentPage * recordsPerPage;
  const indexOfFirstRecord = indexOfLastRecord - recordsPerPage;
  const currentRecords = filteredHistory.slice(
    indexOfFirstRecord,
    indexOfLastRecord
  );

  const totalPages = Math.ceil(filteredHistory.length / recordsPerPage);

  return (
    <div className="container mt-5">
      <div className="card shadow">
        <div className="card-header bg-dark text-white">
          <h3>Prediction History</h3>
        </div>

        <div className="card-body">
          {/* ========================================== */}
          {/* Search Box & Export Button */}
          {/* ========================================== */}

          <div className="row mb-4">
            <div className="col-md-6">
              <input
                type="text"
                className="form-control"
                placeholder="🔍 Search by ID, Prediction or Cluster..."
                value={searchTerm}
                onChange={(e) => setSearchTerm(e.target.value)}
              />
            </div>

            <div className="col-md-6 text-end">
              <button
                type="button"
                className="btn btn-success"
                onClick={exportCSV}
              >
                📥 Export CSV
              </button>
            </div>
          </div>

          <DashboardCards
            total={count}
            highRisk={highRisk}
            lowRisk={lowRisk}
            averageProbability={averageProbability}
          />

          <PredictionCharts
            highRisk={highRisk}
            lowRisk={lowRisk}
            history={history}
          />

          <div className="row mb-4">
            <div className="col-md-6">
              <div className="alert alert-primary">
                <h5>Total Predictions</h5>
                <h2>{count}</h2>
              </div>
            </div>

            <div className="col-md-6">
              {latest && (
                <div className="alert alert-success">
                  <h5>Latest Prediction</h5>

                  <p>
                    <strong>Prediction :</strong> {latest.prediction}
                  </p>

                  <p>
                    <strong>Probability :</strong>{" "}
                    {(latest.probability * 100).toFixed(2)}%
                  </p>
                </div>
              )}
            </div>
          </div>

          {/* ========================================== */}
          {/* Data Table */}
          {/* ========================================== */}

          <table className="table table-bordered table-striped table-hover">
            <thead className="table-dark">
              <tr>
                <th>ID</th>
                <th>Prediction</th>
                <th>Probability</th>
                <th>Cluster</th>
                <th>Date</th>
                <th>Action</th>
              </tr>
            </thead>

            <tbody>
              {filteredHistory.length > 0 ? (
                currentRecords.map((item) => (
                  <tr key={item.id}>
                    <td>{item.id}</td>
                    <td>{item.prediction}</td>
                    <td>{(item.probability * 100).toFixed(2)}%</td>
                    <td>{item.cluster}</td>
                    <td>{new Date(item.created_at).toLocaleString()}</td>
                    <td>
                      <button
                        className="btn btn-primary btn-sm me-2"
                        onClick={() => handleView(item)}
                      >
                        View
                      </button>

                      <button
                        className="btn btn-danger btn-sm"
                        onClick={() => handleDelete(item.id)}
                      >
                        Delete
                      </button>
                    </td>
                  </tr>
                ))
              ) : (
                <tr>
                  <td colSpan="6" className="text-center text-muted">
                    No prediction found.
                  </td>
                </tr>
              )}
            </tbody>
          </table>

          {/* ========================================== */}
          {/* Pagination */}
          {/* ========================================== */}

          <div className="d-flex justify-content-between align-items-center mt-4">
            <button
              className="btn btn-secondary"
              disabled={currentPage === 1}
              onClick={() => setCurrentPage(currentPage - 1)}
            >
              ⬅ Previous
            </button>

            <span className="fw-bold">
              Page {currentPage} of {totalPages || 1}
            </span>

            <button
              className="btn btn-secondary"
              disabled={currentPage === totalPages || totalPages === 0}
              onClick={() => setCurrentPage(currentPage + 1)}
            >
              Next ➡
            </button>
          </div>

          {/* ========================================== */}
          {/* React-Bootstrap Modal */}
          {/* ========================================== */}

          <Modal show={showModal} onHide={closeModal} centered>
            <Modal.Header closeButton>
              <Modal.Title>Prediction Details</Modal.Title>
            </Modal.Header>

            <Modal.Body>
              {selectedPrediction && (
                <>
                  <p>
                    <strong>Prediction:</strong> {selectedPrediction.prediction}
                  </p>

                  <p>
                    <strong>Probability:</strong>{" "}
                    {(selectedPrediction.probability * 100).toFixed(2)}%
                  </p>

                  <p>
                    <strong>Cluster:</strong> {selectedPrediction.cluster}
                  </p>

                  <hr />

                  <h5>Recommendations</h5>

                  <ul>
                    {Array.isArray(selectedPrediction.recommendations) ? (
                      selectedPrediction.recommendations.map((rec, index) => (
                        <li key={index}>{rec}</li>
                      ))
                    ) : (
                      <li>{selectedPrediction.recommendations}</li>
                    )}
                  </ul>
                </>
              )}
            </Modal.Body>

            <Modal.Footer>
              <Button variant="secondary" onClick={closeModal}>
                Close
              </Button>
            </Modal.Footer>
          </Modal>
        </div>
      </div>
    </div>
  );
}

export default PredictionHistory;