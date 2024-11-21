import React, { useState, useEffect } from 'react';
import { Container, Paper, Typography } from '@mui/material';
import SwatchGrid from './components/SwatchGrid';
import ErrorAlert from './components/ErrorAlert';
import { getSwatches } from './services/api';

const ColorSwatchApp = () => {
  const [swatches, setSwatches] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const fetchSwatches = async () => {
    try {
      setLoading(true);
      setError(null);
      const data = await getSwatches();
      setSwatches(data);
    } catch (err) {
      setError('Failed to fetch color swatches');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchSwatches();
  }, []);

  return (
    <Container sx={{ py: 4 }}>
      <Typography variant="h3" component="h1" align="center" gutterBottom>
        Color Swatches
      </Typography>
      <Paper sx={{ p: 3 }}>
        {error && <ErrorAlert message={error} />}
        <SwatchGrid 
          swatches={swatches} 
          loading={loading} 
          onRegenerate={fetchSwatches}
        />
      </Paper>
    </Container>
  );
};

export default ColorSwatchApp;