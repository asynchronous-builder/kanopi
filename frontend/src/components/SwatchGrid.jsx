// src/components/SwatchGrid.jsx
import React from 'react';
import { Box, Button, Grid } from '@mui/material';
import ColorSwatch from './ColorSwatch';

const SwatchGrid = ({ swatches, loading, onRegenerate }) => (
  <Box sx={{ display: 'flex', flexDirection: 'column', gap: 3 }}>
    <Grid container spacing={3} justifyContent="center">
      {swatches.map((color, index) => (
        <Grid item key={index}>
          <ColorSwatch color={color} />
        </Grid>
      ))}
    </Grid>
    <Button 
      variant="contained"
      onClick={onRegenerate}
      disabled={loading}
      sx={{ maxWidth: 300, mx: 'auto' }}
    >
      {loading ? 'Generating...' : 'Generate New Swatches'}
    </Button>
  </Box>
);

export default SwatchGrid;