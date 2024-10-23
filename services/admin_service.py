import aiofiles
from fastapi import FastAPI, File, UploadFile


app = FastAPI()


@app.get("/v2/admin/docs")
async def get_documents(variant: str | None = None):
    if variant:
        # TODO: Filter by variant
        pass
    return [
        {
            "id": 1,
            "name": "full-name",
            "pdf": "path/to/my/pdf.pdf",
            "lines": 1000,
        }
    ]


@app.get("/v2/admins/docs/{doc_id}")
async def get_document_by_id(doc_id: int):
    # TODO: Get documen by id
    doc = {
        "id": 1,
        "name": "full-name",
        "pdf": "path/to/my/pdf.pdf",
        "lines": 1000,
    }
    return doc


@app.post("/v2/admin/docs")
async def create_document(
    csv: UploadFile = File(...), pdf: UploadFile = File(...)
):
    files_dir = "files/"
    csv_path = files_dir + str(csv.filename)
    if csv.size == 0 or pdf.size == 0:
        return {"error": "NO"}
    async with aiofiles.open(csv_path, "wb") as out_file:
        content = await csv.read()
        await out_file.write(content)
    pdf_path = files_dir + str(pdf.filename)
    async with aiofiles.open(pdf_path, "wb") as pdf_file:
        conten = await pdf.read()
        await pdf_file.write(conten)
    return {"csv_name": csv.filename, "pdf_name": pdf.filename}


@app.put("/v2/admin/docs/{doc_id}")
async def update_document(doc_id: int):
    # TODO: Get document by id that will be update
    doc = {
        "id": 1,
        "name": "new-full-name",
        "pdf": "path/to/my/pdf.pdf",
        "lines": 1000,
    }
    return doc


@app.delete("/v2/admin/docs/{doc_id}")
async def delete_document(doc_id: int):
    doc = {
        "id": 1,
        "name": "new-full-name",
        "pdf": "path/to/my/pdf.pdf",
        "lines": 1000,
    }
    return doc
