import { Button, Dialog, DialogPanel, DialogTitle } from "@headlessui/react";

export const RegisterModal = ({
  isOpen,
  handleClose,
}: {
  isOpen: boolean;
  handleClose: () => void;
}) => {
  return (
    <Dialog open={isOpen} as="div" onClose={handleClose}>
      <div className="fixed inset-0 z-10 w-screen overflow-y-auto">
        <div className="flex min-h-full items-center justify-center p-4">
          <DialogPanel
            transition
            // eslint-disable-next-line tailwindcss/no-custom-classname
            className="data-[closed]:transform-[scale(95%)] w-full max-w-md rounded-xl bg-white/5 p-6 backdrop-blur-2xl duration-300 ease-out data-[closed]:opacity-0"
          >
            <DialogTitle as="h3" className="text-base/7 font-medium text-white">
              이상한 루트에요
            </DialogTitle>
            <p className="mt-2 text-sm/6 text-white/50">
              잘못된 방식으로 접근하고 계셔요. 다시 시도해주세요.
            </p>
            <div className="mt-4">
              <Button
                className="inline-flex items-center gap-2 rounded-md bg-gray-700 px-3 py-1.5 text-sm/6 font-semibold text-white shadow-inner shadow-white/10 focus:outline-none data-[hover]:bg-gray-600 data-[open]:bg-gray-700 data-[focus]:outline-1 data-[focus]:outline-white"
                onClick={handleClose}
              >
                닫기
              </Button>
            </div>
          </DialogPanel>
        </div>
      </div>
    </Dialog>
  );
};
