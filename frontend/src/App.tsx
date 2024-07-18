import to from "await-to-js";
import { useRef, useState } from "react";
import Card from "./components/Card";
import ImageUpload from "./components/ImageUpload";
import WritingPad, { WritingPadRef } from "./components/WritingPad";
import styles from "./index.module.scss";
import Image from "./components/Image";

const App = () => {
  const [loading, setLoading] = useState<boolean>(false);
  const [output, setOutput] = useState<File>();
  const [uploadImage, setUploadImage] = useState<File>();

  const writingPad = useRef<WritingPadRef>(null);

  const handleClear = () => {
    if (!writingPad.current) {
      return;
    }
    writingPad.current.clearPad();
    setUploadImage(undefined);
    setOutput(undefined);
  };

  const handleSubmit = async () => {
    setLoading(true);
    await (async () => {
      if (!writingPad.current) {
        return;
      }
      const [err, handwrittenImage] = await to(writingPad.current.getImage());
      if (err) {
        return;
      }
      const formData = new FormData();
      formData.append("input", uploadImage ?? handwrittenImage);
      const [fetchErr, res] = await to(
        fetch("/api/evaluate", {
          method: "POST",
          body: formData,
        })
      );
      if (fetchErr) {
        return;
      }
      const [bufferErr, buffer] = await to(res.arrayBuffer());
      if (bufferErr) {
        return;
      }
      setOutput(new File([buffer], 'image.png', { type: 'image/png' }));
    })();
    setLoading(false);
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
        <Card className={styles["output-card"]}>
          Output:
          <Image file={output} />
        </Card>
      </div>
      {loading && <div className={styles.loading}>Loading...</div>}
    </div>
  );
};

export default App;
