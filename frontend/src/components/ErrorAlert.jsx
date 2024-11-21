// src/components/ErrorAlert.jsx
import React from 'react';
import { Paper, Typography } from '@mui/material';
import { Warning } from '@mui/icons-material';

const ErrorAlert = ({ message }) => (
  <Paper 
    sx={{ 
      p: 2, 
      display: 'flex', 
      alignItems: 'center', 
      gap: 1,
      bgcolor: 'error.light',
      color: 'error.dark'
    }}
  >
    <Warning />
    <Typography>{message}</Typography>
  </Paper>
);

export default ErrorAlert;