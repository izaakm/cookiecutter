# if (!requireNamespace("BiocManager", quietly = TRUE))
# install.packages("BiocManager")
# BiocManager::install("edgeR")

load_or_install_packages = function() {

    list.of.packages <- c(
                          "edgeR",
                          "limma",
                          "modules",
                          "optparse",
                            )

    new.packages <- list.of.packages[!(list.of.packages %in% installed.packages()[,"Package"])]
    if(length(new.packages)) {
        if (!requireNamespace("BiocManager", quietly = TRUE)) {
            install.packages("BiocManager", repos='http://cran.us.r-project.org')
        }
        # BiocManager::install(version = "3.10")
        # The install() function is provided by BiocManager. This is a
        # wrapper around install.packages, but with the repository
        # chosen according to the version of Bioconductor in use, rather
        # than to the version relevant at the time of the release of R.
        # https://bioconductor.org/install/
        BiocManager::install(new.packages)
    }
    # lapply(list.of.packages, require, character.only = TRUE)
    lapply(list.of.packages, require, character.only = TRUE)

}

load_or_install_packages()

# END.
