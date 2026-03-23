from extract import extract_all
from transform import transform
from logger import get_logger
import time

logger = get_logger("pipeline")

def run_pipeline():
  try:
    logger.info("="*30)
    logger.info(f"Started running pipeline cycle")
    start = time.perf_counter()
    logger.info("Step 1/3: extract")
    raw = extract_all()

    logger.info("Step 2/3: transform")
    df = transform(raw)
    
    # logger.info("Step 3/3: load")
  except Exception as e:
    logger.exception(f" - {e}")
    raise
  finally:
    elapsed = time.perf_counter() - start
    logger.info(f"Finished running a pipeline cycle | duration={elapsed:.2f}s")
    logger.info("="*30)

if __name__ == "__main__":
  run_pipeline()
  # scheduler below