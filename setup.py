
import cx_Freeze

arquivo = [cx_Freeze.Executable(
    script="Projeto Game.py", icon="picwish.ico"
)]

cx_Freeze.setup(
    name="Fast and furious favela!",
    options={"build_exe": {"packages": ["pygame"],
                           "include_files": ["assets"]}},
    executables=arquivo
)
