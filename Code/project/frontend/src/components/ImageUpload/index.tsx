import classnames from "classnames";
import {
  ChangeEventHandler,
  DragEventHandler,
  useRef,
  useState
} from "react";
import Image from "../Image";
import styles from "./index.module.scss";

interface ImageUploadProps {
  image: File | undefined;
  setImage: (image: File) => void;
}

const ImageUpload = ({ image, setImage }: ImageUploadProps) => {
  const input = useRef<HTMLInputElement>(null);

  const [isDragOver, setIsDragOver] = useState<boolean>(false);

  const handleClick = () => {
    input.current?.click();
  };

  const handleChange: ChangeEventHandler<HTMLInputElement> = (e) => {
    const files = e.target.files;
    const image = files?.item(0);
    if (!image) {
      return;
    }
    setImage(image);
    e.target.value = "";
  };

  const handleDragOver: DragEventHandler<HTMLDivElement> = (e) => {
    e.preventDefault();
    setIsDragOver(true);
  };

  const handleDragLeave: DragEventHandler<HTMLDivElement> = (e) => {
    e.preventDefault();
    setIsDragOver(false);
  };

  const handleDrop: DragEventHandler<HTMLDivElement> = (e) => {
    e.preventDefault();
    setIsDragOver(false);
    const image = e.dataTransfer.files.item(0);
    if (!image || !image.type.startsWith("image")) {
      return;
    }
    setImage(image);
  };

  return (
    <div className={styles["image-upload"]}>
      <div
        className={classnames(
          styles["drag-area"],
          isDragOver && styles["drag-over"]
        )}
        onClick={handleClick}
        onDragOver={handleDragOver}
        onDragLeave={handleDragLeave}
        onDrop={handleDrop}
      >
        <span>Click or drag image here to upload</span>
      </div>
      <Image file={image} />
      <input
        ref={input}
        className={styles["file-input"]}
        type="file"
        onChange={handleChange}
        accept="image/*"
      />
    </div>
  );
};

export default ImageUpload;
