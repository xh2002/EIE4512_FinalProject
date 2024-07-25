import { debounce } from "lodash-es";
import {
  MouseEventHandler,
  forwardRef,
  useEffect,
  useImperativeHandle,
  useRef,
} from "react";
import styles from "./index.module.scss";

export interface WritingPadRef {
  getImage: () => Promise<File>;
  clearPad: () => void;
}

const WritingPad = forwardRef<WritingPadRef, unknown>((_, ref) => {
  const isWriting = useRef<boolean>();
  const div = useRef<HTMLDivElement>(null);
  const canvas = useRef<HTMLCanvasElement>(null);
  const context = useRef<CanvasRenderingContext2D>();
  const position = useRef<{ x: number; y: number }>({ x: 0, y: 0 });
  const rect = useRef<DOMRect>({
    width: 0,
    height: 0,
    x: 0,
    y: 0,
    left: 0,
    right: 0,
    top: 0,
    bottom: 0,
    toJSON: () => {},
  });

  const handleMouseDown: MouseEventHandler<HTMLCanvasElement> = (e) => {
    isWriting.current = true;
    position.current.x = e.clientX - rect.current.x;
    position.current.y = e.clientY - rect.current.y;
  };

  const handleMouseMove: MouseEventHandler<HTMLCanvasElement> = (e) => {
    if (!canvas.current || !context.current || !isWriting.current) {
      return;
    }
    context.current.beginPath();
    context.current.moveTo(position.current.x, position.current.y);
    context.current.lineWidth = 20;
    context.current.lineCap = "round";
    position.current.x = e.clientX - rect.current.x;
    position.current.y = e.clientY - rect.current.y;
    context.current.lineTo(position.current.x, position.current.y);
    context.current.stroke();
  };

  const handleMouseUp: MouseEventHandler<HTMLCanvasElement> = () => {
    isWriting.current = false;
  };

  useEffect(() => {
    if (!canvas.current) {
      return;
    }
    const ctx = canvas.current.getContext("2d");
    if (!ctx) {
      return;
    }
    context.current = ctx;
  }, []);

  useEffect(() => {
    if (!div.current) {
      return;
    }
    const observer = new ResizeObserver(
      debounce((entries) => {
        if (!canvas.current || !context.current) {
          return;
        }
        rect.current = entries[0].target.getBoundingClientRect();
        const _canvas = document.createElement("canvas");
        _canvas.width = canvas.current.width;
        _canvas.height = canvas.current.height;
        _canvas.getContext("2d")?.drawImage(canvas.current, 0, 0);
        const scaleX = rect.current.width / canvas.current.width;
        const scaleY = rect.current.height / canvas.current.height;
        canvas.current.width = rect.current.width;
        canvas.current.height = rect.current.height;
        context.current.scale(scaleX, scaleY);
        context.current.drawImage(_canvas, 0, 0);
        context.current.scale(1 / scaleX, 1 / scaleY);
      }, 300)
    );
    observer.observe(div.current);
    return () => {
      observer.disconnect();
    };
  }, []);

  useImperativeHandle(ref, () => ({
    getImage: () =>
      new Promise((resolve) => {
        if (!canvas.current) {
          return;
        }
        canvas.current.toBlob((blob) => {
          if (!blob) {
            return;
          }
          resolve(new File([blob], "image.png", { type: "image/png" }));
        });
      }),
    clearPad: () => {
      if (!context.current) {
        return;
      }
      context.current.clearRect(0, 0, rect.current.width, rect.current.height);
    },
  }));

  return (
    <div className={styles["writing-pad"]} ref={div}>
      <canvas
        ref={canvas}
        onMouseDown={handleMouseDown}
        onMouseMove={handleMouseMove}
        onMouseUp={handleMouseUp}
      />
    </div>
  );
});

export default WritingPad;
