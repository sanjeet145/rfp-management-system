import Button from '@mui/material/Button';

export default function IconButton({icon,name,func}) {
  return (
      <Button onClick={func} variant="contained" endIcon={icon}>
        {name}
      </Button>
  );
}
