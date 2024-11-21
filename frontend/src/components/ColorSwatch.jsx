// src/components/ColorSwatch.jsx
import React from 'react';
import { Box, Paper, Typography } from '@mui/material';

const ColorSwatch = ({ color }) => {
  const getBackgroundColor = () => {
    switch (color.type) {
      case 'rgb':
        return `rgb(${color.red}, ${color.green}, ${color.blue})`;
      case 'hsl':
        return `hsl(${color.hue}, ${color.saturation}%, ${color.lightness}%)`;
      case 'brgb':
        return `rgb(${Math.round(color.red * 255 / 10000)}, ${Math.round(color.green * 255 / 10000)}, ${Math.round(color.blue * 255 / 10000)})`;
      default:
        return '#000';
    }
  };

  const formatValue = (key, value) => {
    switch (color.type) {
      case 'brgb':
        return Math.round(value);
      case 'hsl':
        return key === 'hue' ? Math.round(value) : `${value}%`;
      default:
        return value;
    }
  };

  return (
    <Box sx={{ display: 'flex', flexDirection: 'column', gap: 1 }}>
      <Paper 
        elevation={3}
        sx={{
          width: 128,
          height: 128,
          backgroundColor: getBackgroundColor(),
          transition: 'transform 0.2s',
          '&:hover': {
            transform: 'scale(1.05)'
          }
        }}
      />
      <Box sx={{ fontSize: '0.875rem' }}>
        {Object.entries(color)
          .filter(([key]) => key !== 'type')
          .map(([key, value]) => (
            <Box key={key} sx={{ display: 'flex', justifyContent: 'space-between', mb: 0.5 }}>
              <Typography variant="body2" sx={{ fontWeight: 500, textTransform: 'capitalize' }}>
                {key}:
              </Typography>
              <Typography variant="body2">
                {formatValue(key, value)}
              </Typography>
            </Box>
          ))}
      </Box>
    </Box>
  );
};

export default ColorSwatch;