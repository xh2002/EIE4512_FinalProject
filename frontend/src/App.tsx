import { useRef, useState } from "react";
import Card from "./components/Card";
import ImageUpload from "./components/ImageUpload";
import WritingPad, { WritingPadRef } from "./components/WritingPad";
import styles from "./index.module.scss";
import to from "await-to-js";

const App = () => {
  const [result, setResult] = useState<number>();
  const [image, setImage] = useState<File>();

  const writingPad = useRef<WritingPadRef>(null);

  const handleClear = () => {
    if (!writingPad.current) {
      return;
    }
    setImage(undefined);
    writingPad.current.clearPad();
  };

  const handleSubmit = async () => {
    if (!writingPad.current) {
      return;
    }
    const [err, res] = await to(writingPad.current.getImage());
    if (err) {
      return;
    }
    console.log("手写板图片", res);
    console.log("上传图片", image);
    // TODO: 调后端拿结果
    setResult(Math.floor(Math.random() * 10));
  };

  return (
    <div className={styles.container}>
      <Card className={styles.left}>
        <WritingPad ref={writingPad} />
      </Card>
      <div className={styles.right}>
        <Card className={styles["upload-card"]}>
          <ImageUpload image={image} setImage={setImage} />
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
