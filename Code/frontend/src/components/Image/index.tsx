import { useMemo } from 'react';
import styles from './index.module.scss'

interface ImageProps {
  file?: File;
}

const Image = ({ file }: ImageProps) => {
  const url = useMemo(
    () => (file ? URL.createObjectURL(file) : undefined),
    [file]
  );

  return url && <img className={styles.image} src={url} />;
};

export default Image;
