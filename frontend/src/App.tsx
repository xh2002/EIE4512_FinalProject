import { useRef, useState } from "react";
import Card from "./components/Card";
import ImageUpload from "./components/ImageUpload";
import WritingPad, { WritingPadRef } from "./components/WritingPad";
import styles from "./index.module.scss";
import to from "await-to-js";

const App = () => {
  const [result, setResult] = useState<number>();
  const [uploadImage, setUploadImage] = useState<File>();

  const writingPad = useRef<WritingPadRef>(null);

  const handleClear = () => {
    if (!writingPad.current) {
      return;
    }
    setUploadImage(undefined);
    writingPad.current.clearPad();
  };

  const handleSubmit = async () => {
    if (!writingPad.current) {
      return;
    }
    const [err, handwrittenImage] = await to(writingPad.current.getImage());
    if (err) {
      return;
    }
    const formData = new FormData();
    formData.append("image", uploadImage ?? handwrittenImage);
    const [fetchErr, res] = await to(
      fetch("http://localhost:8000/api", {
        method: "POST",
        body: formData,
      })
    );
    if (fetchErr) {
      return;
    }
    const [jsonErr, json] = await to(res.json());
    if (jsonErr) {
      return;
    }
    setResult(json.output);
  };

  return (
    <div className={styles.container}>
      <Card className={styles.left}>
        <WritingPad ref={writingPad} />
      </Card>
      <div className={styles.right}>
        <Card className={styles["upload-card"]}>
          <ImageUpload image={uploadImage} setImage={setUploadImage} />
          <div className={styles.buttons}>
            <button className={styles.button} onClick={handleClear}>
              Clear
            </button>
            <button className={styles.button} onClick={handleSubmit}>
              Submit
            </button>
          </div>
        </Card>
        <Card>Result: {result}</Card>
      </div>
    </div>
  );
};

export default App;
